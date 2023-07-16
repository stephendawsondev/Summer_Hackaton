"""
Imports
"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
# Internal
# Register your models here.
from .models import Place, Challenge, Answer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """
    Admin model class For register model
    """
    list_display = (
        'title',
        'created_on',
        )
    prepopulated_fields = {
        'slug': ('title',)
        }
    search_fields = [
        'title',
        'image',
        ]
    list_filter = (
        'title',
        'created_on'
        )


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    """
    Admin model class For register model
    """
    list_display = (
        'quiz',
        'created_on'
        )
    prepopulated_fields = {
        'slug': ('quiz',)
        }
    search_fields = [
        'quiz'
        ]
    list_filter = (
        'quiz',
        'created_on'
        )
    

@admin.register(Answer)
class QuestionAdmin(admin.ModelAdmin):
    """
    Admin model class For register model
    """
    list_display = (
        'text',
        'created_on',
        'confirmation'
        )
