from django.shortcuts import render
from .models import Testimonial, Website

def home(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request, 'webpages/home.html', context=context)

def camp(request):
    return render(request, 'webpages/camp.html')

def website(request):
    websites = Website.objects.all()
    return render(request, 'webpages/website.html', context={'title': 'Team Websites', 'websites': websites})