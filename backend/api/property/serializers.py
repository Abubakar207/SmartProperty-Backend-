from ast import Delete
from pyexpat import model
from rest_framework import serializers
from .models import Property

class PropertySerilizers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
    
    def create(self, validated_data):
        return super().create(validated_data)
    def update(self, instance, validated_data):
        instance.Purpose = validated_data.get('Purpose',instance.Purpose)
        instance.Propertytype = validated_data.get('Propertytype',instance.Propertytype)
        instance.PropertySubtype = validated_data.get('PropertySubtype',instance.PropertySubtype)
        instance.City = validated_data.get('City',instance.City)
        instance.Location = validated_data.get('Location',instance.Location)
        instance.ZipCode = validated_data.get('ZipCode',instance.ZipCode)
        instance.PropertyTitle = validated_data.get('PropertyTitle',instance.PropertyTitle)
        instance.Description = validated_data.get('Description',instance.Description)
        instance.LandArea = validated_data.get('LandArea',instance.LandArea)
        instance.Unit = validated_data.get('Unit',instance.Unit)
        instance.UserId = validated_data.get('UserId',instance.UserId)

        instance.save()
        return instance

    
    
   
   
