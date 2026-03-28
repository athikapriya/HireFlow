from rest_framework import serializers
from .models import Application


# =============== application serializers =============== 
class ApplicationSerializer(serializers.ModelSerializer):
    candidate = serializers.StringRelatedField(read_only=True)
    job = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = ["id", "job", "candidate", "resume", "cover_letter", "applied_at", "status"]