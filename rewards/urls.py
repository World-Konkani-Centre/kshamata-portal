from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('give_award/',give_award , name='give_award'),
    path('toplist/', top_list, name='top_list'),
    path('leaderboard/',leaderboard,name="leaderboard"),
]
