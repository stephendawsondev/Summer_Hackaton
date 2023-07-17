"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from challenge.models import Answer
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Profile(models.Model):
    """
    Profile model
    """
    done = models.ManyToManyField(Answer, related_name='answers_done',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        """
        Items Order
        """
        ordering = [
            '-created_on'
            ]
    def __str__(self):
        """
        Return Title
        """
        return str(self.points)
