from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
    """
    Class representing a deck of flash-cards in the database.
    """
    name = models.CharField(max_length=60)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
