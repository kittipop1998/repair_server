# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# # from userprofile.views import UserProfileViewSet
#
# router = DefaultRouter()
# router.register(r'user-profile')
#
# urlpatterns = [
#     path('', include(router.urls))
# ]
from django.urls import path, include
from rest_framework import routers, viewsets
from userprofile import views as userprofile_models

router = routers.DefaultRouter()
router.register('user-profile', userprofile_models.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]