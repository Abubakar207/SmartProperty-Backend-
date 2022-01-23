from telnetlib import STATUS
from django.shortcuts import render
from h11 import Response
from rest_framework import viewsets
from .models import PropertyImages
from .serilizers import PropertyImagesSerilizers
# Create your views here.

class PropertyImageViewSets(viewsets.ModelViewSet):
    queryset = PropertyImages.objects.all()
    serializer_class = PropertyImagesSerilizers