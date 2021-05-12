from django.urls import path

from .views import *

urlpatterns = [
    path('give_award/',give_award , name='give_award'),
    path('list/', award_list, name='list'),
    path('leaderboard/',leaderboard,name="leaderboard"),
]
