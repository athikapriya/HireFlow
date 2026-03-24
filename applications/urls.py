from django.urls import path
from . import views

urlpatterns = [
    path("candidate/apply/<int:job_id>/", views.apply_job, name="apply_job"),
    path("candidate/applied-jobs/", views.applied_jobs, name="applied_jobs"),

    path('employer/all_applications/', views.employer_applications, name='employer_applications'),
    path('employer/application/<int:app_id>/accept/', views.accept_application, name='accept_application'),
    path('employer/application/<int:app_id>/reject/', views.reject_application, name='reject_application'),
]