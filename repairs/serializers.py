from rest_framework import serializers
from .models import Repair, RepairType


class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = ['status_choices', 'contact', 'desc',
                  'status', 'request_date',
                  'completed_data', 'approve_data',
                  'image', 'user', 'repair_type', ]


class RepairTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairType
        fields = ['name']
