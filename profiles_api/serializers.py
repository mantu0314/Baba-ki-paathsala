from rest_framework import serializers

from profiles_api import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','phone','password','confirm_password','age','status')
        extra_kwargs={
        'password':{'write_only':True},
        'style':{'input-type':'password'}
        }

    def create(self,validated_data):
        user=models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        phone=validated_data['phone'],
        password=validated_data['password'],
        confirm_password=validated_data['confirm_password'],
        age=validated_data['age'],
        status=validated_data['status']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
