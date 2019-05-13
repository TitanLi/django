# POST
> 因安全考量會出現Forbidden (CSRF cookie not set.) 403

> 可將settings.py
>> django.middleware.csrf.CsrfViewMiddleware 註解即可

## 在一般情況下使用
1. APP-NAME/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /update/post/
    path('post/', views.post, name='post'),
]
```
2. APP-NAME/views.py
```
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import json

def post(request):
    if request.method == 'POST':
        print("POST")
        data = json.loads(request.body)['post-key']
        print(data)
    
    return HttpResponse(data)
```
## 當使用x-www-form-urlencoded
> request.META.get('CONTENT_TYPE') = application/x-www-form-urlencoded
1. 編輯urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /update/
    path('', views.index, name='index'),
]
```
2. 編輯views.py
```
from django.http import JsonResponse
import json

def index(request):
    if request.method == 'POST':
        print("POST")
        print(request.POST['csrfmiddlewaretoken'])
        data = request.POST['csrfmiddlewaretoken']
    
    return JsonResponse({"data":data})
```