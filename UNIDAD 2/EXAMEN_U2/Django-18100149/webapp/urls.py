from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('', views.index, name='index'),
    path('animals_details', views.animals_details, name='animalsdetails'),
    path('create/', views.create, name='create'),
    path('detail/<int:animal_id>/', views.read, name='read'),
    path('update/<int:animal_id>/', views.update, name='update'),
    path('delete/<int:animal_id>/', views.delete, name='delete'),
]
