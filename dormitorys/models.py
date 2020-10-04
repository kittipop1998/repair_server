from django.db import models
from userprofile import models as userprofile_models
import uuid


class Dormitory(models.Model):
    nameDo = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nameDo)


class RoomType(models.Model):
    nameTy = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nameTy)


class Room(models.Model):
    nameRo = models.CharField(max_length=255)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.SET_NULL, null=True, blank=True)
    # user_profile = models.ForeignKey(userprofile_models.UserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.room_type)
