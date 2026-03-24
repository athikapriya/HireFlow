from django.urls import path
from . import views

urlpatterns = [
    path("apply/<int:job_id>/", views.apply_job, name="apply_job"),
    path("applied-jobs/", views.applied_jobs, name="applied_jobs"),
]