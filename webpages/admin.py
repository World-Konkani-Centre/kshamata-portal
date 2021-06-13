from django.contrib import admin
from .models import Testimonial, Website, Event, Post, Comment, Banner, Visibility, Schedule, Registration
# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    actions = None


@admin.register(Visibility)
class VisibilityAdmin(admin.ModelAdmin):
    actions = None


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    actions = None


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass