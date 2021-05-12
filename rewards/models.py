from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum
from PIL import Image

from users.models import Team

OPTIONS = (
    ("1", "FIRST"),
    ("2", "SECOND"),
    ("3", "THIRD"),
    ("4", "NONE"),
)


class Points(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    heading = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=OPTIONS, default='4')
    points = models.IntegerField(default=0)
