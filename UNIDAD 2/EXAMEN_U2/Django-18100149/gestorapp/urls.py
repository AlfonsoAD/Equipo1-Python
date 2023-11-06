from django.urls import path
from . import views

app_name = 'consultations'

urlpatterns = [
    path('', views.index, name='index'),
    path("doctors", views.index_doctors, name="index_doctors"),
    path("clinics", views.index_clinics, name="index_clinics"),
    path('create/', views.create, name='create'),
    path('detail/<int:consultation_id>/', views.read, name='read'),
    path('update/<int:consultation_id>/', views.update, name='update'),
    path('delete/<int:consultation_id>/', views.delete, name='delete'),
]
