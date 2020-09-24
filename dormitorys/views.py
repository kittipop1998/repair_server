from django.shortcuts import render
from dormitorys import models, serializers
from rest_framework import viewsets


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializers_class = serializers.RoomSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = models.RoomType.objects.all()
    serializers_class = serializers.RoomTypeSerializer
    

class DormitoryViewSet(viewsets.ModelViewSet):
    queryset = models.Dormitory.objects.all()
    serializer_class = serializers.DormitorySerializer
