from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:team_id>/', views.detail, name='detail'),
    path('<int:team_id>/edit/', views.edit, name='edit'),
    path('<int:team_id>/delete/', views.delete, name='delete'),
]
