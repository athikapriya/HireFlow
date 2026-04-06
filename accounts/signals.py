from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
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

        try:
            if settings.ENV == "production":
                logger.info("Skipping email in production (no SMTP)")
            else:
                send_welcome_email.delay(instance.email, instance.username)

        except Exception as email_error:
            logger.error(f"Email failed: {email_error}")

    except Exception as e:
        logger.error(f"Signal error: {e}")