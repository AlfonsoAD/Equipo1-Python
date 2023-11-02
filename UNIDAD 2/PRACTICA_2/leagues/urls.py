from django.urls import path
from . import views

app_name = 'leagues'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:league_id>/', views.detail, name='detail'),
    path('edit/<int:league_id>/', views.edit, name='edit'),
    path('delete/<int:league_id>/', views.delete, name='delete'),
]
