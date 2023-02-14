from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('head', views.head, name='head'),
    path('staffs', views.staff, name='staff'),
    path('department', views.department, name='department'),
   
]