
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
