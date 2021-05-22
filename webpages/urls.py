from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('camp/', camp, name='camp'),
    path('teams', website, name='team-website'),
    path('events/', submit, name='submit'),
    path('sotp', sotp, name='sotp'),
    path('camp-register', camp_register, name='camp-register'),
    path('schedule/', schedule, name='schedule'),
    path('wishes/<id>', blog_single, name='blog-detail'),
    path('wishes', blog, name='blog'),
]