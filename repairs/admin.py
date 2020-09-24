from django.contrib import admin
from . import models


class RepairAdmin(admin.ModelAdmin):
    list_display = [
        'status_choices', 'contact', 'desc',
        'status', 'request_date',
        'completed_data', 'approve_data',
        'repair_type', 'user', 'image',
    ]


class RepairTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


admin.site.register(models.RepairType)
admin.site.register(models.Repair)
