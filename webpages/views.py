from users.views import my_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial, Website, Form
from django.contrib.auth.decorators import login_required


def home(request):
    testimonial = Testimonial.objects.all()

    context = {
        'testimonial': testimonial,
        'title': 'HOME'
    }
    return render(request, 'webpages/home.html', context=context)

@login_required
def camp(request):
    return render(request, 'webpages/camp.html', context={'title': 'LEADERSHIP EXPERIENCES'})

@login_required
def schedule(request):
    return render(request, 'webpages/schedule.html', context={'title': 'SCHEDULE', 'display': False})

@login_required
def website(request):
    websites = Website.objects.all()
    return render(request, 'webpages/website.html', context={'title': 'TEAMS', 'websites': websites, 'display': False})

@login_required
def submit(request):
    form = Form.objects.all()
    return render(request, 'webpages/submit.html', context={'title': 'SUBMIT', 'forms': form , 'display': False})

@login_required
def sotp(request):
    return render(request, 'webpages/sotp.html', context={'title': 'SOTP', 'display': False})


def camp_register(request):
    messages.error(request, 'Please login to register for these camps.')
    return redirect('login')
