from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('<int:video_id>/', views.vlog_video, name='vlog_video'),
        ]
