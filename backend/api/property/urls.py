from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register('property', views.PropertyViewSets)

urlpatterns = [
    path('', include(router.urls))
]
