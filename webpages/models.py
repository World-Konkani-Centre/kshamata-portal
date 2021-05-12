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