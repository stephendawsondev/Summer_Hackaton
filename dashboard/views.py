"""
Imports
"""
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3rd party:
from django.shortcuts import render
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create your views here.
def index(request):
    """
    Home page view
    """
    return render(request, "dashboard/index.html")


def rules(request):
    """
    Rules page view
    """
    return render(request, "rules/rules.html")

def leaderboard(request):
    """
    Rules page view
    """
    return render(request, "leaderboard/leaderboard.html")
