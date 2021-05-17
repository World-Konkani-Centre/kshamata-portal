from django.contrib import admin
from .models import Profile, Team, User
from django.contrib.auth.admin import UserAdmin
from csv_export.views import CSVExportView


class UserAdminClass(UserAdmin):
    # list to display in admin panel
    actions = ('export_data_csv',)
    list_display = ('email', 'name', 'batch', 'college_name')
    # search by following fields
    search_fields = ('email', 'batch', 'name', 'college_name')
    # cannot be edited
    readonly_fields = ()

    # required features that should be overriding the UserAdmin,
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    def export_data_csv(self, request, queryset):
        view = CSVExportView(queryset=queryset, fields='__all__')
        return view.get(request)

    export_data_csv.short_description = 'Export CSV for selected Data records'


admin.site.register(User, UserAdminClass)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
