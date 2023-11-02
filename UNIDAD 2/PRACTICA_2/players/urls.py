from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:player_id>/', views.detail, name='detail'),
    path('<int:player_id>/edit/', views.edit, name='edit'),
    path('<int:player_id>/delete/', views.delete, name='delete'),
]
