from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum
from PIL import Image

from users.models import Team


class Type(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(default='default.jpg', upload_to='badge_image')

    def __str__(self):
        return f'{self.name}'


class Points(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    heading = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
