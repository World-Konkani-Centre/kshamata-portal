from django import forms
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from rewards.models import Type
from users.models import Team


class MultiBadgeForm(forms.Form):
    choices = []
    for i in User.objects.all().order_by(Lower('profile__name')):
        name = str(i.profile.name) + '  (' + str(i.profile.team) + ')'
        entry = (i.id, name)
        choices.append(entry)
    choices = tuple(choices)

    profiles = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, required=False)
    teams = forms.ModelChoiceField(queryset=Team.objects.all(), required=False)
    heading = forms.CharField(max_length=100)
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    points = forms.IntegerField(required=True)
    show = forms.BooleanField(required=True, help_text="Select only for top 3, which will be shown in the awards list")
