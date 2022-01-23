from pyexpat import model
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id']