"""
Imports
"""
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3rd party:
from django.shortcuts import render
# Internal
from .models import Question, Challenge, Place
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def challenge(request, id):
    """
    Challenge page view
    """
    challenges = Challenge.objects.filter(place = id).values()
    questions = Question.objects.all()
    context = {
        "challenges": challenges,
        "questions": questions,
    }

    return render(request, "challenge/challenge.html", context)


def location(request):
    """
    locations page view
    """
    places = Place.objects.all()
    context = {
        "places": places,
    }

    return render(request, "location/location.html", context)


def question(request, id):
    """
    question page view
    """
    questions = Question.objects.filter(challenge = id).values()
    context = {
        "questions": questions,
    }

    return render(request, "question/question.html", context)
