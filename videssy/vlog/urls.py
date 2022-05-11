"""
These url paths handle the routing logic for video creation, viewing, liking,
commenting, deleting as well as channel and subscription related pages. Any 
and all views mentioned here can be found in the views.py file in the same directory.
"""
from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.HomeView.as_view(), name='home'),
        path('watch/<slug:slug>/', views.VideoPlayerView.as_view(), name='video_player'),
        path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
        path('create_video/', views.CreateVideoView.as_view(), name='create_video'),
        path('delete_video/<slug:video_slug>/', views.delete_video, name='delete_video'),
        path('like_video/<slug:video_slug>/', views.like_video, name='like_video'),
        path('comments/<slug:video_slug>/', views.comments, name='comments'),
        path('search/<str:search_str>', views.search, name='search'),
        path('liked_videos/', views.liked_videos, name='liked_videos'),
        path('subscriptions/', views.subscriptions, name='subscriptions'),
        ]
