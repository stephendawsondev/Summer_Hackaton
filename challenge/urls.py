# Imports
# 3rd party:
from django.urls import path, include
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('locations/', views.location, name="location"),
    path('challenge/<int:id>/', views.challenge, name="challenge"),
    path('json/<int:id>/', views.challenge_json, name="challengeJson"),
    path('answers/<int:id>/', views.answer, name="answer"),
    path('change-score/', views.change_score, name="changeScore"),
    path('check/', views.checkanswer, name="checkanswer"),
    path('challenges/json', views.all_challenges_json, name="allChallengesJson"),
]
