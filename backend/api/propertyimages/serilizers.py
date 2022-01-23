from pyexpat import model
from rest_framework import serializers
from .models import PropertyImages

class PropertyImagesSerilizers(serializers.ModelSerializer):
    image1 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    image2 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    image3 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    image4 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    image5 = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    class Meta:
        model = PropertyImages
        fields = '__all__'
   