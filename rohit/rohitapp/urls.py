from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rohit', views.hello, name='index1'),
]
