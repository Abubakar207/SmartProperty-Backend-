from email.mime import image
from django.db import models
from api.property.models import Property
# Create your models here.
class PropertyImages(models.Model):
     image1 = models.ImageField(upload_to='images/')
     image2 = models.ImageField(upload_to='images/')
     image3 = models.ImageField(upload_to='images/', blank=True, null=True)
     image4 = models.ImageField(upload_to='images/', blank=True, null=True)
     image5 = models.ImageField(upload_to='images/', blank=True, null=True)
     property = models.ForeignKey(Property, on_delete=models.SET_NULL,blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)