from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    image = models.ImageField(upload_to='testimonial')
    testimonial = models.TextField()

    def __str__(self):
        return f'{self.name} Testimonial'


class Website(models.Model):
    name = models.CharField(max_length=50, help_text='Team name')
    image = models.ImageField(upload_to='team_website', help_text='Upload the team logo')
    url = models.URLField(help_text='Team website URL')

    def __str__(self):
        return f'{self.name} Website'


class Form(models.Model):
    name = models.CharField(max_length=50, help_text='Form name')
    url = models.URLField(help_text='Form URL')
    deadline = models.CharField(max_length=100, help_text='Enter deadline in human readbale format for ex. 12/2 8:00 PM')
    description = models.TextField(help_text='A brief description on Form')

    def __str__(self):
        return f'{self.name} Form'  