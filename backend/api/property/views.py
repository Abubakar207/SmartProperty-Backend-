from django.shortcuts import render
from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerilizers
# Create your views here.

class PropertyViewSets(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerilizers