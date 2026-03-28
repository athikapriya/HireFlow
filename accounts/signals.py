from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import User


@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):

    if created:
        if instance.role == 'candidate' and not instance.designation:
            User.objects.filter(pk=instance.pk).update(designation="Candidate")

        elif instance.role == 'employer' and not instance.designation:
            User.objects.filter(pk=instance.pk).update(designation="Employer")

        Token.objects.create(user=instance)

        print(f"New user created: {instance.username} ({instance.role})")