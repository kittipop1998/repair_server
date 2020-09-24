from django.urls import path, include
from rest_framework import routers, viewsets
from userprofile import views as userprofile_models

router = routers.DefaultRouter()
router.register('user-profile', userprofile_models.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]