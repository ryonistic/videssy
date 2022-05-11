"""
These url paths handle the routing logic for authentication as well 
as channel and subscription related pages. Any and all views mentioned 
here can be found in the views.py file in the same directory.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path("channel/<str:username>/", views.user_detail_view, name="detail"),
    path("subscribe/<str:username>/", views.subscribe, name="subscribe"),
]
