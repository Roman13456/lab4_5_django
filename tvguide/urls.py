from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('channels/', views.channel_list, name='channel_list'),
    path('channels/<int:channel_id>/', views.channel_detail, name='channel_detail'),
    path('programs/', views.program_list, name='program_list'),
]
