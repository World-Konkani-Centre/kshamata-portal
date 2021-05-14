from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('camp/', camp, name='camp'),
    path('team-website', website, name='team-website'),
    path('submit/', submit, name='submit'),
    path('sotp', sotp, name='sotp'),
    path('camp-register', camp_register, name='camp-register')
]