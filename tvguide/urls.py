from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Channel URLs
    path('channels/', views.channel_list, name='channel_list'),
    path('channels/<int:pk>/', views.channel_detail, name='channel_detail'), # Changed channel_id to pk for consistency
    # CRUD paths for Channels
    path('channels/new/', views.channel_create, name='channel_create'), # New Channel CRUD
    path('channels/<int:pk>/edit/', views.channel_update, name='channel_update'), # New Channel CRUD
    path('channels/<int:pk>/delete/', views.channel_delete, name='channel_delete'), # New Channel CRUD
    # Program URLs
    path('programs/', views.program_list, name='program_list'),
    # CRUD paths for Programs
    path('programs/new/', views.program_create, name='program_create'),
    path('programs/<int:pk>/edit/', views.program_update, name='program_update'),
    path('programs/<int:pk>/delete/', views.program_delete, name='program_delete'),
]
