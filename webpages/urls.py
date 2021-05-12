from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('camp/', camp, name='camp')
]