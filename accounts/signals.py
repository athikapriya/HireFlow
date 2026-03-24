
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):

    if created:
        if instance.role == 'candidate' and not instance.designation:
            instance.designation = "Candidate"
            instance.save()
        elif instance.role == 'employer' and not instance.designation:
            instance.designation = "Employer"
            instance.save()

        print(f"New user created: {instance.username} ({instance.role})")