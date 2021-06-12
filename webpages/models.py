from django.db import models
from users.models import User, Camp


class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    image = models.ImageField(upload_to='testimonial')
    testimonial = models.TextField()

    def __str__(self):
        return f'{self.name} Testimonial'


class Website(models.Model):
    camp = models.ForeignKey(Camp, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text='Team name')
    image = models.ImageField(upload_to='team_website', help_text='Upload the team logo')
    url = models.URLField(help_text='Team website URL')

    def __str__(self):
        return f'{self.name} Website'


class Event(models.Model):
    camp = models.ForeignKey(Camp, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text='Event name')
    time = models.CharField(max_length=50, help_text='Event Timings, Leave it blank if not needed', blank=True, null=True)
    description = models.TextField(blank=True, null=True, help_text='Event Description, Leave it blank if not needed')
    image = models.ImageField( upload_to='events', help_text='Event Photo',)

    def __str__(self):
        return f'{self.name} Form'  


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ImageField(upload_to='blog-post-thumbnail')

    def __str__(self):
        return f"Post {self.title}"

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Comment"


class Banner(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    register = models.ImageField(upload_to='Banners', verbose_name='Register Page Banner')
    schedule = models.ImageField(upload_to='Banners', verbose_name='Schedule Page Banner')
    teams = models.ImageField(upload_to='Banners', verbose_name='Team Page Banner')
    campers = models.ImageField(upload_to='Banners', verbose_name='Campers Page Banner')
    leaderboard = models.ImageField(upload_to='Banners', verbose_name='Leaderboard Page Banner')
    awards = models.ImageField(upload_to='Banners', verbose_name='Award Page Banner')
    events = models.ImageField(upload_to='Banners', verbose_name='Event Page Banner')



class Visibility(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    schedule = models.BooleanField(help_text='Tick if you want to make schedule page visible to all')
    teams = models.ImageField(help_text='Tick if you want to make teams page visible to all')
    campers = models.ImageField(help_text='Tick if you want to make campers page visible to all')
    leaderboard = models.ImageField(help_text='Tick if you want to make leaderboard page visible to all')
    awards = models.ImageField(help_text='Tick if you want to make awards page visible to all')
    events = models.ImageField(help_text='Tick if you want to make events page visible to all')

    