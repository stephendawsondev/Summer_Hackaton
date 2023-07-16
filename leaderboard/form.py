from django import forms
from .models import Profile

class ProfileForm(forms.Form):
    """
    profile Form
    """
    score = forms.IntegerField(label="score")