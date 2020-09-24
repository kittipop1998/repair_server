from rest_framework import serializers
from .models import Room, RoomType, Dormitory


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['nameRo']


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['nameTy']


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = ['nameDo']
