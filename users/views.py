import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileUpdateForm, UserUpdateForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

from .models import Profile


def email_check(user_cred):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, user_cred):
        return True
    else:
        return None


# login
def my_login(request):
    if request.POST:
        user_cred = request.POST['username']
        print(user_cred)
        password = request.POST['password']
        user = authenticate(request, email=user_cred, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged into your account!!')
            return redirect('index')

        else:
            messages.error(request, 'Invalid Credential')
            return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'authorization/login.html', {'title': "Login"})


# register
def my_register(request):
    if request.POST:
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}')
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
def members(request):
    p = Profile.objects.all()
    return render(request, 'profile/members.html', context={'profile': p})
