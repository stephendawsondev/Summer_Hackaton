"""
Imports
"""
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3rd party:
from django.shortcuts import render, redirect
# Internal
from .models import Answer, Challenge, Place
from django.http import JsonResponse
from leaderboard.models import Profile

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def challenge(request, id):
    """
    Challenge page view
    """
    challenges = Challenge.objects.filter(place=id).values()
    city = Place.objects.filter(id=id).values("city").first()
    answers = Answer.objects.all()
    context = {
        "challenges": challenges,
        "answers": answers,
        "city": city,
    }

    return render(request, "challenge/challenge.html", context)


def challenge_json(request, id):
    """
    Challenge page view
    """
    challenges = Challenge.objects.filter(place=id).first()
    city = Place.objects.filter(id=id).values("city")
    answers = Answer.objects.all()
    context = {
        "challenges": challenges,
        "answers": answers,
        "city": city,
    }
    return JsonResponse({"coordinates": challenges.cordinates})


def location(request):
    """
    locations page view
    """
    places = Place.objects.all()
    if not places:
        places = {"none": "none"}
    context = {
        "places": places,
    }

    return render(request, "location/location.html", context)


def answer(request, id):
    """
    answer page view
    """
    challenges = Challenge.objects.filter(place=id).values()
    answers = Answer.objects.filter(challenge=id).all()
    city = Place.objects.filter(id=id).values("city").first()
    context = {
        "challenges": challenges,
        "answers": answers,
        "city": city,
    }

    return render(request, "answer/answer.html", context)


def change_score(request):
    """
    change_score page view
    """
    score = request.POST['score']
    userId = request.POST['userId']

    user_points = Profile.objects.filter(user=userId).first()

    user_points.points += int(score)
    user_points.save()

    return redirect("leaderboard")
