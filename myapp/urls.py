from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/', views.doctor_single, name='doctor_single'),
    path('hospital/', views.hospital_single, name='hospital_single'),
]