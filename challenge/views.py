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
from django.contrib.auth.models import User

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
    Api json file to cordinates
    """
    challenges = Challenge.objects.filter(place=id).first()
    return JsonResponse({"coordinates": challenges.cordinates})

def all_challenges_json(request):
    """
    Api json challenge
    """
    challenges = Challenge.objects.all()

    return JsonResponse([challenge.serialize() for challenge in challenges], safe=False)


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
    challenges = Challenge.objects.filter(id=id).first()
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


def checkanswer(request):
    """
    change_score page view
    """
    answerID = request.POST['answer']
    userId = request.POST['userId']
    answer = Answer.objects.get(pk=answerID)
    user_profile = Profile.objects.filter(user=userId).first()
    userRef = User.objects.get(pk=userId)
    flag=True
    for done in user_profile.done.all():
        if (answer == done) : 
            flag = False
    print( flag)
    if (answer.confirmation is True) and flag :
        user_profile.done.add(answer)        
        answer.save()
        user_profile.points += 5
        user_profile.save()
        return redirect("leaderboard")
    else:
        return redirect("location")
