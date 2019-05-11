# params
參考資料：[https://docs.djangoproject.com/en/2.2/intro/tutorial03/](https://docs.djangoproject.com/en/2.2/intro/tutorial03/)
## view
編輯APP-NAME/views.py
```
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def detail(request, question_id1):
    return HttpResponse("You're looking at question %s." % question_id1)

def results(request, question_id1, question_id2):
    response = "You're looking at the results of question %s + %s."
    return HttpResponse(response % (question_id1,question_id2))

def vote(request, question_id1, question_id2, question_id3):
    return HttpResponse("You're voting on question %s + %s + %s." % (question_id1,question_id2,question_id3))
```
## URL
編輯APP-NAME/urls.py
資料格式化：[https://officeguide.cc/python-string-formatters-tutorial/](https://officeguide.cc/python-string-formatters-tutorial/)
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /update/
    path('', views.index, name='index'),
    # ex: /update/1/
    path('<int:question_id1>/', views.detail, name='detail'),
    # ex: /update/1/2/results/
    path('<int:question_id1>/<int:question_id2>/results/', views.results, name='results'),
    # ex: /update/1/2/3/vote/
    path('<int:question_id1>/<int:question_id2>/<int:question_id3>/vote/', views.vote, name='vote'),
]
```