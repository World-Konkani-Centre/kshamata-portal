from django.contrib import admin
from .models import Profile, Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass