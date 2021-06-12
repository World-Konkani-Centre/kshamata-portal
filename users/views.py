import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileUpdateForm, UserUpdateForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

from .models import Profile
from webpages.utils import return_camp_id
from webpages.models import Banner


# register
def my_register(request):
    if request.POST:
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            messages.success(request,
                             f'You have successfully registered for SOTP 2021. You can login now with your email: {username}')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'authorization/register.html', context)


# logout
def my_logout(request):
    logout(request)
    return redirect('index')


@login_required
def my_profile(request):
    global u_form, p_form, profile
    user = get_object_or_404(User, id=request.user.id)

    if request.POST:
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user,
        'title': "Profile",
    }
    return render(request, 'profile/profile.html', context=context)


# show all them members in the profile
@login_required
def members(request, camp):
    camp_id = return_camp_id(camp)
    p_1 = Profile.objects.filter(role='Committee').order_by('user__name')
    p_2 = Profile.objects.filter(role='Camper', camps=camp_id).order_by('user__name')
    image = Banner.objects.filter(camp=camp_id).first().campers

    context = {
        'committee': p_1,
        'campers': p_2,
        'banner': image,
        'camp_id': camp_id
    }
    return render(request, 'profile/members.html', context=context)
