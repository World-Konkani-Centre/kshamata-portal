from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def camp(request):
    return render(request, 'webpages/camp.html')