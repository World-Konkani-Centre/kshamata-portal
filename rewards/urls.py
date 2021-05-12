from django.urls import path

from .views import *

urlpatterns = [
    path('award/',give_award , name='give_award'),
    path('award-list/', award_list, name='award-list'),
    path('leaderboard/',leaderboard,name="leaderboard"),
]
