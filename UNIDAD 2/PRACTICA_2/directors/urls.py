from django.urls import path
from . import views

app_name = 'directors'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:director_id>/', views.detail, name='detail'),
    path('<int:director_id>/edit/', views.edit, name='edit'),
    path('<int:director_id>/delete/', views.delete, name='delete'),
]
