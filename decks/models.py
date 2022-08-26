from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
    """
    Class representing a deck of flash-cards in the database.
    """
    name = models.CharField(max_length=60)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Card(models.Model):
    """
    Class representing a card with a `front` and a `back` field.
    Each card must be attached to one deck.
    """
    front = models.CharField(max_length=400)
    back = models.CharField(max_length=400)

    deck = models.ForeignKey(to=Deck, on_delete=models.CASCADE)
