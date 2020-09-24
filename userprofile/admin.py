from django.contrib import admin
from userprofile import models as userprofile_models

admin.site.register(userprofile_models.UserProfile)
