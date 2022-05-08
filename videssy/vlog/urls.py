from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.HomeView.as_view(), name='home'),
        path('watch/<slug:slug>/', views.VideoPlayerView.as_view(), name='video_player'),
        path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
        path('create_video/', views.CreateVideoView.as_view(), name='create_video'),
        path('like_video/<slug:video_slug>/', views.like_video, name='like_video'),
        path('comments/<slug:video_slug>/', views.comments, name='comments'),
        ]
