from django.db import models
from django.conf import settings


# =============== Skill model =============== 
class Skill(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name



# =============== job model =============== 
class Job(models.Model):
    EMPLOYMENT_CHOICES = (
        ("FT", "Full-time"),
        ("PT", "Part-time"),
        ("CT", "Contract"),
        ("IN", "Internship"),
        ("FL", "Freelance"),
    )

    EXPERIENCE_REQUIRED = (
        ("0-1 year", "0-1 Year"),
        ("2 years", "2 Years"),
        ("3 years", "3 Years"),
        ("4 years", "4 Years"),
        ("5 years or above", "5 Years or above"),
        )

    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="job_posted")
    
    company_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)

    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    employment_type = models.CharField(max_length=2, choices=EMPLOYMENT_CHOICES, default="FT")
    experience = models.CharField(max_length=50, choices=EXPERIENCE_REQUIRED, default="0-1 year")

    company_logo = models.ImageField(upload_to="company_logos/", null=True, blank=True)

    skills = models.ManyToManyField(Skill, related_name="jobs")

    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["is_active", "-posted_at"]

    def __str__(self):
        return f"{self.title} at {self.location} - {self.company_name}"