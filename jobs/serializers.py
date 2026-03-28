from rest_framework import serializers
from .models import Job, Skill


# =============== skills serializers =============== 
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]


# =============== job serializers =============== 
class JobSerializer(serializers.ModelSerializer):
    employer = serializers.StringRelatedField(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ["id", "title", "company_name", "location", "salary",
                  "employment_type", "experience", "company_logo",
                  "skills", "posted_at", "deadline", "is_active", "employer"]