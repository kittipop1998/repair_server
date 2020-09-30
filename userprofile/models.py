from django.db import models
from django.contrib.auth.models import User
from dormitorys.models import Room


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.TextField()
    branch = models.TextField()
    Room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user
