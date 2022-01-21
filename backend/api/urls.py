from django.urls import path, include
from django.http import JsonResponse
def home(request):
    return JsonResponse({'Page Name': 'API'})
urlpatterns = [
    path('', home),
    path('user/', include('api.user.urls')),
]
