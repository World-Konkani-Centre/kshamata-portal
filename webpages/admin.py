from django.contrib import admin
from .models import Testimonial, Website, Form
# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    pass