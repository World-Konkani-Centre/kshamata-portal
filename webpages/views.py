from django.shortcuts import render
from .models import Testimonial, Website, Form

def home(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial,
        'title': 'Home'
    }
    return render(request, 'webpages/home.html', context=context)

def camp(request):
    return render(request, 'webpages/camp.html', context={'title': 'LEADERSHIP EXPERIENCES'})

def website(request):
    websites = Website.objects.all()
    return render(request, 'webpages/website.html', context={'title': 'Team Websites', 'websites': websites})

def submit(request):
    form = Form.objects.all()
    return render(request, 'webpages/submit.html', context={'title': 'Submit forms', 'forms': form})

def sotp(request):
    return render(request, 'webpages/sotp.html', context={'title': 'SOTP'})