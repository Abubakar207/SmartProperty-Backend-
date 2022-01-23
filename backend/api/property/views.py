from functools import partial
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.http import JsonResponse
from .models import Property
from .serializers import PropertySerilizers
from rest_framework.views import APIView

# Create your views here.


class PropertyApi(APIView):
    def get(self,request,format=None,pk=None):
        id =pk
        if id is not None:
            if Property.objects.filter(pk=id).exists():
                property = Property.objects.get(id=id)
                serializers = PropertySerilizers(property)
                return JsonResponse(serializers.data,safe=False)
            return JsonResponse({'error':'No Recored Found'},safe=False)
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
       return JsonResponse({'error':'No Recored Found'},safe=False)
       
       
    def patch(self,request,pk=None,format=None):
        id = pk
        if Property.objects.filter(pk=id).exists():
           property = Property.objects.get(pk=id)
           serializers = PropertySerilizers(property ,data=request.data,partial=True)
           if serializers.is_valid():
                serializers.save()
                return JsonResponse({'Success':"Your Property detail is successfuly updated..!"},safe=False)
           return JsonResponse({'error':serializers.errors},safe=False)
        return JsonResponse({'error':'No Recored Found'},safe=False)
    def delete(self,request,format=None,pk=None):
       print('print')
    #    if Property.objects.get(pk=id).exists():
       property = Property.objects.get(id=pk).delete()
       return JsonResponse({'Success':"Your Property ads is successfuly deleted..!"},safe=False)          
       #return JsonResponse({'error':'No  Del Recored Found'},safe=False)
    #    return JsonResponse({'Success':"Your Property ads is successfuly deleted..!"},safe=False)
#   Subtype add in property
       



            
                
            

            