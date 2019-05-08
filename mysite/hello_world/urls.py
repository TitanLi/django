from django.urls import path

from . import views

urlpatterns = [
    path('123', views.index, name='index'),
]