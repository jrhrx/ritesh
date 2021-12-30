from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from k2 import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='login'),
]
