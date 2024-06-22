from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password','user_type']
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class FileUploadSerialzer(serializers.ModelSerializer):
    class Meta:
        model=FileUpload
        fields=['file']