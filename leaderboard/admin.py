"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
# Internal
# Register your models here.
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin model class For register model
    """
    list_display = (
        'points',
        )