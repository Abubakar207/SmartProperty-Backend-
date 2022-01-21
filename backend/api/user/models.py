from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name =models.CharField(max_length=50,default='anonymous')
    email = models.CharField(max_length=250,unique=True)

    #username = None
    #USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

    #Additional
    otp = models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    cnic = models.CharField(max_length=20,blank=True,null=True)
    gender = models.CharField(max_length=20,blank=True,null=True)
    session_token = models.CharField(max_length=10,default=0)
    jwt_token = models.CharField(max_length=255,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
