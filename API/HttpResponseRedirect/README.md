# HttpResponseRedirect
1. 編輯APP-NAME/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /update/
    path('', views.index, name='index'),
    path('aaa/', views.aaa, name='aaa'),
]
```
2. 編輯APP-NAME/views.py
```
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question

def index(request):
    return HttpResponseRedirect(reverse('aaa'))

def aaa(request):
    return HttpResponse('aaa')
```