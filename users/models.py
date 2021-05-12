from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum
from PIL import Image


class Team(models.Model):
    name = models.CharField(max_length=100)
    team_points = models.IntegerField(default=0)
    url = models.URLField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    batch = models.IntegerField(null=True,blank=True)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,null=True,blank=True)
    college = models.CharField(max_length=100,null=True,blank=True)
    points = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

