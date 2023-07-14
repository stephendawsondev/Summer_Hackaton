"""
Imports
"""
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3rd party:
from django.shortcuts import render
# Internal
from .models import Question, Challenge, Place
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create your views here.
def challenge(request):
    """
    Home page view
    """
    places = Place.objects.all()
    challenges = Challenge.objects.all()
    questions = Question.objects.all()
    context = {
        "places": places,
        "challenges": challenges,
        "questions": questions,
    }

    return render(request, "challenge/challenge.html", context)
