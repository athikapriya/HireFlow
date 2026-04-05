from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import User
from .tasks import send_welcome_email
from decouple import config
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if not created:
        return

    try:
        if not instance.designation:
            instance.designation = "Candidate" if instance.role == "candidate" else "Employer"
            instance.save(update_fields=["designation"])

        Token.objects.create(user=instance)

        if config("ENV", default="local") == "production":
            send_welcome_email(instance.email, instance.username)
        else:
            send_welcome_email.delay(instance.email, instance.username)

    except Exception as e:
        logger.error(f"Error in user_created_handler signal: {e}")