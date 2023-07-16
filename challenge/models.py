"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Place(models.Model):
    """
    Place model
    """

    country = models.CharField(max_length=50, unique=False)
    city = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=50, unique=False)
    title = models.CharField(max_length=50, unique=False)
    image = CloudinaryField('image',default='placeholder')
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
        return str(self.title)


class Challenge(models.Model):
    """
    Challenge Class
    """
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=False)
    quiz = models.CharField(max_length=100, unique=False)
    cordinates =  models.CharField(max_length=100, unique=False)
    description = models.CharField(max_length=250, unique=False)
    image = CloudinaryField('image',default='placeholder')
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
        Return Quiz question
        """
        return str(self.quiz)

    def serialize(self):
        """
        Serialize the item
        """
        return {
            "slug": self.slug,
            "quiz": self.quiz,
            "cordinates": self.cordinates,
            "description": self.description,
            "created_on": self.created_on,
            "image": ("https://res.cloudinary.com/herokupp4/image/upload/v1689526831/"+ str(self.image)),
            }


class Answer(models.Model):
    """
    Questions Class
    """
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    text = models.CharField(max_length=250, unique=False)
    created_on = models.DateTimeField(auto_now_add=True)
    confirmation = models.BooleanField()
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
        return str(self.text)
