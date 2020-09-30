from django.shortcuts import render
from rest_framework import viewsets
from userprofile import models as userprofile_models


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = userprofile_models.UserProfile
    queryset = userprofile_models.UserProfile.objects.all()