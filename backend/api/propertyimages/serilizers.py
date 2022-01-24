from asyncio.windows_events import NULL
from email.mime import image
from pyexpat import model
from rest_framework import serializers
from .models import PropertyImages

class PropertyImagesSerilizers(serializers.ModelSerializer):
    image1 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False, required=True)
    image2 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False, required=True)
    image3 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    image4 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    image5 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    class Meta:
        model = PropertyImages
        fields = '__all__'
    # def validate(self, attrs):
    #         image1 = attrs.get('image1')
    #         if image1 is NULL:
    #             raise serializers.ValidationError('Image1 is required')
    #         image2 = attrs.get('image2')
    #         if image2 is NULL:
    #              raise serializers.ValidationError('Image2 is required')
    #         return attrs

           
        
       
        

    
   