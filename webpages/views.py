from django.shortcuts import render
from .models import Testimonial

def home(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request, 'webpages/home.html', context=context)

def camp(request):
    return render(request, 'webpages/camp.html')