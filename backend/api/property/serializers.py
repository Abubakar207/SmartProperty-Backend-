from pyexpat import model
from rest_framework import serializers
from .models import Property

class PropertySerilizers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
   
   
