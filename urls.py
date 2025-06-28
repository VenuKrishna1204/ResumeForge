# resume/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_resume/', views.generate_resume, name='generate_resume'),
]