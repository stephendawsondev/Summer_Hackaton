"""
Imports
"""
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3rd party:
from django.shortcuts import render
# Internal
from .models import Answer, Challenge, Place
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def challenge(request, id):
    """
    Challenge page view
    """
    challenges = Challenge.objects.filter(place = id).values()
    city = Place.objects.filter(id = id).values("city")
    answers = Answer.objects.all()
    try:
        city = city[0]['city']
    except ValueError:
        print("Error validation")

    context = {
        "challenges": challenges,
        "answers": answers,
        "city": city,
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


def answer(request, id):
    """
    answer page view
    """
    answers = Answer.objects.filter(challenge = id).values()
    context = {
        "answers": answers,
    }

    return render(request, "answer/answer.html", context)
