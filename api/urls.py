from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('jobs/', views.job_list, name='api-job-list'),
    path('jobs/<int:pk>/', views.job_detail, name='api-job-detail'),
    path('jobs/<int:job_id>/apply/', views.apply_job, name='api-job-apply'),
    path('employer/applications/', views.employer_applications),
    path('applications/<int:pk>/', views.update_application_status),
    path('users/<int:pk>/', views.user_detail),
    path('auth/token/', obtain_auth_token, name='api-token-auth'),
]