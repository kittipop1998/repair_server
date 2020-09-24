from django.urls import path, include
from rest_framework import routers
from repairs import views

router = routers.DefaultRouter()
router.register('', views.RepairViewSet)

urlpatterns = [
    path('', include(router.urls))
]
