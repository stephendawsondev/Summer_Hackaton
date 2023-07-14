"""
Imports
"""
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3rd party:
from django.shortcuts import render
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create your views here.
def challenge(request):
    """
    Home page view
    """
    return render(request, "challenge/challenge.html")
