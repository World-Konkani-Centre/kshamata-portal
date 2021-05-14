from django.contrib import admin

# Register your models here.
from rewards.models import Points, Type


@admin.register(Points)
class PointsAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass
