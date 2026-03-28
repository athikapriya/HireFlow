from rest_framework import serializers
from .models import User


# =============== user serializers =============== 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "role", "designation", "profile_image"]