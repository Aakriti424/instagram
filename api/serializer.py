from rest_framework import serializers
from rest_framework.response import Response

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email','mobile_number','password','full_name','username','gender','birth_date']

    def create(self, validated_data):
        user=User.objects.create_user(
            email=validated_data['email'],
            mobile_number=validated_data['mobile_number'],
            password=validated_data['password'],
            full_name=validated_data['full_name'],
            username=validated_data['username'],
            gender=validated_data['gender'],
            birth_date=validated_data['birth_date']
        )
        return user

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Story
        fields=['story','text','tag']



