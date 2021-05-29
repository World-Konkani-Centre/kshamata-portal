from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect

from users.models import Profile, Team, User
from .forms import MultiBadgeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Points


@login_required
def give_award(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            form = MultiBadgeForm()
            return render(request, 'award/give_award.html', context={'form': form})
        else:
            form = MultiBadgeForm(request.POST)
            if form.is_valid():
                users = form.cleaned_data.get('users')
                teams = form.cleaned_data.get('teams')
                heading = form.cleaned_data.get('heading')
                pr_type = form.cleaned_data.get('type')
                points = form.cleaned_data.get('points')
                show = form.cleaned_data.get('show')
                if len(users) != 0:
                    for user in users:
                        Points.objects.create(user=user, heading=heading, type=pr_type, points=points, show=show)
                elif teams:
                    Points.objects.create(team=teams, heading=heading, type=pr_type, points=points, show=show)
                return redirect('give_award')
    else:
        raise Http404()


# display the list of points given including only top 3
def award_list(request):
    awards = Points.objects.filter(show=True)
    users = awards.filter(team=None)
    teams = awards.filter(user=None)
    return render(request, 'award/award_list.html', {"teams": teams, 'users': users, 'display': False})


# show the leaderboard of teams and profiles use points in corresponding models to order
def leaderboard(request):
    team_profiles = ""
    team_points = ""
    profiles = Profile.objects.filter().order_by('-points')[:10]
    teams = Team.objects.filter().order_by("-team_points")[:10]
    if request.user.profile.team:
        team_profiles = Profile.objects.filter(team=request.user.profile.team).order_by('-points')
        team_points = Team.objects.get(id=request.user.profile.team.id)

    return render(request, 'award/leaderboard.html',
                  {'profiles': profiles, 'teams': teams, 'team_profiles': team_profiles, 'team_details': team_points, 'display': False})
