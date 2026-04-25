from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q


from .forms import CandidateRegisterForm, EmployerRegisterForm, CandidateProfileForm, EmployerProfileForm
from applications.models import Application
from jobs.models import Job
from .decorators import candidate_required, employer_required


# =============== employer register view =============== 
def employer_register(request):

    form = EmployerRegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.role = "employer"
        user.save()
        login(request, user)
        return redirect("login")
    
    context = {
        "form" : form
    }

    return render(request, "accounts/register.html", context)



# =============== candidate register view =============== 
def candidate_register(request):

    form = CandidateRegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.role = "candidate"
        user.save()
        login(request, user)
        return redirect("login")
    
    context = {
        "form" : form
    }

    return render(request, "accounts/register.html", context)



# =============== login view =============== 
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.role == "employer":
                return redirect("employer_dashboard")
            else:
                return redirect("candidate_dashboard")
        else:
            messages.error(request, "Invalid username or password")

    context = {

    }
    return render(request, 'accounts/login.html', context)



# =============== logout view =============== 
def logout_user(request):
    logout(request)
    return redirect("login")



# =============== employer dashboard view ===============
@login_required(login_url="login")
@employer_required
def employer_dashboard(request):
    page_title = "Dashboard"
    query = request.GET.get("q")

    jobs = Job.objects.filter(employer=request.user)

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    jobs = jobs.annotate(application_count=Count('applications')).order_by('-updated_at')

    total_jobs = jobs.count()
    active_jobs = jobs.filter(is_active=True).count()
    closed_jobs = jobs.filter(is_active=False).count()

    latest_jobs = jobs[:5]

    total_applications = Application.objects.filter(job__in=jobs).count()
    total_hired = Application.objects.filter(job__in=jobs, status="accepted").count()
    total_rejected = Application.objects.filter(job__in=jobs, status="rejected").count()
    total_pending = Application.objects.filter(job__in=jobs, status="pending").count()

    recent_applications = Application.objects.filter(
        job__employer=request.user
    ).select_related('candidate', 'job').order_by('-applied_at')

    if query:
        recent_applications = recent_applications.filter(
            Q(job__title__icontains=query) |
            Q(candidate__username__icontains=query)
        )

    recent_applications = recent_applications[:7]

    pie_labels = ["Jobs", "Applications", "Hired", "Rejected", "Pending"]
    pie_data = [
        total_jobs,
        total_applications,
        total_hired,
        total_rejected,
        total_pending
    ]

    context = {
        "jobs": latest_jobs,
        "total_jobs": total_jobs,
        "active_jobs": active_jobs,
        "closed_jobs": closed_jobs,

        "total_applications": total_applications,
        "total_hired": total_hired,
        "total_rejected": total_rejected,
        "total_pending": total_pending,

        "pie_labels": pie_labels,
        "pie_data": pie_data,

        "recent_applications": recent_applications,

        "page_title": page_title,
        "query": query,
        "show_topbar_search": True,
    }

    return render(request, 'accounts/employer_dashboard.html', context)


# =============== candidate dashboard view ===============
@login_required(login_url="login")
@candidate_required
def candidate_dashboard(request):
    page_title = "Dashboard"
    user = request.user

    query = request.GET.get("q", "").strip()

    total_applied = Application.objects.filter(candidate=user).count()
    total_accepted = Application.objects.filter(candidate=user, status="accepted").count()
    total_pending = Application.objects.filter(candidate=user, status="pending").count()
    total_rejected = Application.objects.filter(candidate=user, status="rejected").count()

    recent_applications = Application.objects.filter(
        candidate=user
    ).select_related('job', 'job__employer')

    if query:
        recent_applications = recent_applications.filter(
            Q(job__title__icontains=query) |
            Q(job__description__icontains=query) |
            Q(job__employer__username__icontains=query)
        )

    recent_applications = recent_applications.order_by('-applied_at')[:5]

    applied_job_ids = Application.objects.filter(
        candidate=user
    ).values_list('job_id', flat=True)

    jobs_qs = Job.objects.filter(is_active=True).exclude(id__in=applied_job_ids)

    if query:
        jobs_qs = jobs_qs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(employer__username__icontains=query)
        )

    user_skills = []
    if user.skills:
        user_skills = [s.strip().lower() for s in user.skills.split(",")]

    if user_skills:
        skill_query = Q()
        for skill in user_skills:
            skill_query |= Q(skills__name__icontains=skill)

        jobs_qs = jobs_qs.filter(skill_query).distinct()

    recommended_jobs = jobs_qs[:6]

    def calculate_match(job, user_skills):
        job_skills = [s.name.lower() for s in job.skills.all()]
        if not job_skills:
            return 0
        matched = len(set(job_skills) & set(user_skills))
        return int((matched / len(job_skills)) * 100)

    for job in recommended_jobs:
        job.match_score = calculate_match(job, user_skills)

    today = timezone.now().date()
    upcoming_deadline = today + timedelta(days=3)

    context = {
        "page_title": page_title,

        "total_applied": total_applied,
        "total_accepted": total_accepted,
        "total_pending": total_pending,
        "total_rejected": total_rejected,

        "recent_applications": recent_applications,
        "recommended_jobs": recommended_jobs,

        "today": today,
        "upcoming_deadline": upcoming_deadline,

        "query": query,
        "show_topbar_search": True,
    }

    return render(request, 'accounts/candidate_dashboard.html', context)


# =============== profile view =============== 
@login_required(login_url="login")
def profile_view(request):
    user = request.user
    page_title = "My Profile"

    context = {
        "page_title": page_title,
        "user": user,
    }
    return render(request, 'accounts/profile_view.html', context)


# =============== employer profile settings view =============== 
@login_required(login_url="login")
@employer_required
def employer_profileSettings(request):
    page_title = "Profile Settings"

    if request.method == "POST":
        form = EmployerProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = EmployerProfileForm(instance=request.user)

    context = {
        "page_title": page_title,
        "form": form,
    }
    return render(request, 'accounts/profile_form.html', context)



# =============== candidate profile settings view =============== 
@login_required(login_url="login")
@candidate_required
def candidate_profileSettings(request):
    page_title = "Profile Settings"

    if request.method == "POST":
        form = CandidateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = CandidateProfileForm(instance=request.user)

    context = {
        "page_title": page_title,
        "form": form,
    }
    return render(request, 'accounts/profile_form.html', context)