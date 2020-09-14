from django.contrib import admin
from . import models

admin.site.register(models.Dormitory)
admin.site.register(models.RoomType)
admin.site.register(models.Room)
