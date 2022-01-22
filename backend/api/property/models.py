from asyncio.windows_events import NULL
from unicodedata import name
from django.db import models
from api.user.models import CustomUser
# Create your models here.
class Property(models.Model):
    Purpose = models.CharField(max_length=50)
    Propertytype = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Location = models.CharField(max_length=255,blank=False)
    ZipCode = models.IntegerField(blank=False)
    PropertyTitle = models.CharField(max_length=50,blank=False)
    Description = models.CharField(max_length=255,blank=True)
    Price = models.IntegerField(blank=False)
    LandArea = models.IntegerField(blank=False)
    Unit = models.CharField(max_length=255,blank=False)
    UserName = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.Purpose