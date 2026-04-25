from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import RegexValidator


# =============== User model =============== 
class User(AbstractUser):

    phone_validator = RegexValidator(
        regex=r'^\d{11}$',
        message="Phone number must be exactly 11 digits."
    )
    
    ROLE_CHOICES = (
        ("candidate", "Candidate"),
        ("employer", "Employer"),
    )

    username = models.CharField(max_length=150, unique=True)
    designation = models.CharField(max_length=25, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_image = CloudinaryField('image', blank=True, null=True)

    phone = models.CharField(max_length=11, null=True, blank=True, validators=[phone_validator])
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    # employer
    company_name = models.CharField(max_length=150)
    company_logo = CloudinaryField('image')
    company_website = models.URLField(null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)

    # candidate
    skills = models.TextField(null=True, blank=True)
    experience_years = models.IntegerField(null=True, blank=True)
    education = models.CharField(max_length=200, null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.role} - {self.username}'