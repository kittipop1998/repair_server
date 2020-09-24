from django.urls import path, include
from rest_framework import routers
from dormitorys import views

router = routers.DefaultRouter()
router.register('', views.DormitorysViewSet)

urlpatterns = [
    path('', include(router.urls))
]