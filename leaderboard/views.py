"""
Imports
"""
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3rd party:
from django.shortcuts import render
from django.contrib.auth.models import User
# Internal
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def leaderboard(request):
    """
    Rules page view
    """
    users = User.objects.all()
    scores = Profile.objects.all()
    context = {
        'users': users,
        'scores': scores,
    }
    return render(request, "leaderboard/leaderboard.html", context)

def my_points(request, id):
    """
    Rules page view
    """
    users = User.objects.filter(id=id).first()
    scores = Profile.objects.filter(user=id).first()
    context = {
        'users': users,
        'scores': scores,
    }
    return render(request, "leaderboard/mypoints.html", context)
