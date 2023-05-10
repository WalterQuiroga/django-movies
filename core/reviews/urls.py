from django.contrib import admin
from django.urls import path
from .views import ReviewView


urlpatterns = [
    path('', ReviewView.as_view(), name='movie'),
    
]