# JsonResponse
1. urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /update/
    path('', views.index, name='index'),
]
```
2. views.py
```
from django.http import JsonResponse
import json

def index(request):
    if request.method == 'POST':
        print("POST")
        data = json.loads(request.body)['post-key']
        print(data)
    
    return JsonResponse({"data":data})
```