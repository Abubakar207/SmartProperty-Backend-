from argparse import Action
from functools import partial
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.http import JsonResponse
from .models import Property
from .serializers import PropertySerilizers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


    
   

class PropertyApi(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request,format=None,pk=None):
        
        id =pk
        if id is not None:
            if Property.objects.filter(pk=id).exists():
                property = Property.objects.get(id=id)
                serializers = PropertySerilizers(property)
                return JsonResponse(serializers.data,safe=False)
            return JsonResponse({'error':'No Record Found'},safe=False)
        property = Property.objects.all()
        serializers = PropertySerilizers(property,many=True)
        return JsonResponse(serializers.data,safe=False)
 
    def post(self,request,format=None):
       serializers = PropertySerilizers(data=request.data)
       if serializers.is_valid():
           serializers.save()
           return JsonResponse({'Success':"Your Property detail is successfuly added..!"},safe=False)
       return JsonResponse({'error':serializers.errors},safe=False)
    def put(self,request,pk=None,format=None):
       id = pk
       if Property.objects.filter(pk=id).exists():
           property = Property.objects.get(pk=id)
           serializers = PropertySerilizers(property ,data=request.data)
           if serializers.is_valid():
                serializers.save()
                return JsonResponse({'Success':"Your Property detail is successfuly updated..!"},safe=False)
           return JsonResponse({'error':serializers.errors},safe=False)
       return JsonResponse({'error':'No Record Found'},safe=False)
       
       
    def patch(self,request,pk=None,format=None):
        id = pk
        if Property.objects.filter(pk=id).exists():
           property = Property.objects.get(pk=id)
           serializers = PropertySerilizers(property ,data=request.data,partial=True)
           if serializers.is_valid():
                serializers.save()
                return JsonResponse({'Success':"Your Property detail is partialy updated..!"},safe=False)
           return JsonResponse({'error':serializers.errors},safe=False)
        return JsonResponse({'error':'No Record Found'},safe=False)
    def delete(self,request,format=None,pk=None):
       id = pk
       if Property.objects.get(pk=id) is not None:
           property = Property.objects.get(pk=id).delete()
           return JsonResponse({'Success':"Your Property ads is successfuly deleted..!"},safe=False)          
       return JsonResponse({'error':'No  Record Found'},safe=False)
