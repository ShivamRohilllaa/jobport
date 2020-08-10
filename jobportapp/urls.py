from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('clgdet/', views.clgdet, name='College Details'),
    path('<int:id>/', views.update_data, name='updateprof'),
]