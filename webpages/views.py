from users.views import my_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Testimonial, Website, Event, Post
from django.contrib.auth.decorators import login_required
from .forms import CommentForm


def home(request):
    testimonial = Testimonial.objects.all()

    context = {
        'testimonial': testimonial,
        'title': 'HOME'
    }
    return render(request, 'webpages/home.html', context=context)


@login_required
def camp(request):
    return render(request, 'webpages/camp.html', context={'title': 'KSHAMATA CAMPS'})


@login_required
def schedule(request):
    return render(request, 'webpages/schedule.html', context={'title': 'SCHEDULE', 'display': True})


@login_required
def website(request):
    websites = Website.objects.all()
    return render(request, 'webpages/website.html', context={'title': 'TEAMS', 'websites': websites, 'display': True})


@login_required
def submit(request):
    form = Event.objects.all()
    return render(request, 'webpages/submit.html', context={'title': 'Events', 'events': form , 'display': True})


@login_required
def sotp(request):
    return render(request, 'webpages/sotp.html', context={'title': 'SOTP', 'display': False})


def camp_register(request):
    messages.error(request, 'Please login to register for these camps.')
    return redirect('login')


def blog(request):
    post = Post.objects.all()
    context = {
        'queryset': post,
        'title': 'WISHES'
    }
    return render(request, 'blog/blog.html', context)


def blog_single(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            messages.success(request, 'Your Message is Posted')
            return redirect(request.META['HTTP_REFERER'])

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/blog-single.html', context=context)
