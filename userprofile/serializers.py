from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from . import models as userprofile_models


class CustomRegisterSerializer(RegisterSerializer):
    board = serializers.CharField(max_length=225)
    branch = serializers.CharField(max_length=225)
    dormitory_number = serializers.CharField(max_length=10)
    dormitory_name = serializers.IntegerField()
    Room_number = serializers.CharField(max_length=5)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')
        user.save(update_fields=['first_name', 'last_name'])


class UserProfile(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = userprofile_models.UserProfile
        exclude = ('password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')


class CustomUserDetailsSerializer(UserDetailsSerializer):
    profile = UserProfile(source='userprofile', read_only=True, required=False)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile',)
        read_only_fields = ('profile',)
