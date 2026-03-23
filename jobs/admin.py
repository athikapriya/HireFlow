from django.contrib import admin
from .models import Job, Skill


# ================= Skill Admin =================
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# ================= Job Admin =================
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "employer",
        "employment_type",
        "experience",
        "deadline",
        "is_active",
        "get_skills", 
    )
    
    list_filter = (
        "employment_type",
        "experience",
        "is_active",
        "deadline",
    )
    
    search_fields = ("title", "location", "employer__username")
    ordering = ("-posted_at",)

    def get_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])
    get_skills.short_description = "Skills"