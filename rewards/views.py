from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from users.models import Profile, Team
from .forms import MultiBadgeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# give award, preferably like multi badge
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
                profiles = form.cleaned_data.get('profiles')
                teams = form.cleaned_data.get('teams')
                heading = form.cleaned_data.get('heading')
                type = form.cleaned_data.get('type')
                points = form.cleaned_data.get('points')
                show = form.cleaned_data.get('show')
                # if len(profiles) != 0:
                #     for id in profiles:
                #         Points.objects.create(user=get_object_or_404(User, id=int(id)), heading=heading, type=type,
                #                               points=points, show=show)
                # elif teams:
                #     Points.objects.create(team=teams, heading=heading, type=type, points=points, show=show)
                # print(id)
                # print(teams)
                # print(heading)
                # print(type)
                # print(points)
                # print(show)
    else:
        raise Http404()


# display the list of points given including only top 3
def award_list(request):
    awards = Points.objects.filter(show=False)
    return render(request, 'award/award_list.html', {"awards": awards})


# show the leaderboard of teams and profiles use points in corresponding models to order
def leaderboard(request):
    profiles = Profile.objects.filter().order_by('-points')
    teams = Team.objects.filter().group_by("-team_points")
    return render(request, 'award/leaderboard.html', {'profiles': profiles, 'teams': teams})
