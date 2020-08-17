from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('profdet/', views.Profdet, name='Profile'),
    path('clgdet/', views.clgdet, name='College'),
    path('<int:id>/', views.update_data, name='update'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
]