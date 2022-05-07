from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.HomeView.as_view(), name='home'),
        path('watch/<slug:slug>/', views.VideoPlayerView.as_view(), name='video_player'),
        path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
        ]
