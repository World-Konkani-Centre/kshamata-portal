from django.contrib import admin
from .models import Profile, Team
from django.contrib.auth.admin import UserAdmin


class UserAdminClass(UserAdmin):
    # list to display in admin panel
    list_display = ('email', 'name', 'batch', 'college_name')
    # search by following fields
    search_fields = ('email', 'batch', 'name', 'college_name')
    # cannot be edited
    readonly_fields = ()

    # required features that should be overriding the UserAdmin,
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
