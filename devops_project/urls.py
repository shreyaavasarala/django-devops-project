from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('docker/', views.docker_page),
    path('cicd/', views.cicd_page),
    path('architecture/', views.architecture_page),
    path('about/', views.about_page),
]