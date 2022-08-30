from typing import Any

from rest_framework import generics
from django.db.models import QuerySet

from decks.models import Deck

from .models import Card
from .serializer import CardSerializer


class CardListCreateView(generics.ListCreateAPIView):
    """

    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @property
    def deck(self) -> Any | None:
        """"""
        id = self.kwargs.get('deck')
        return Deck.objects.filter(id=id).first()
        # TODO check if user is owner

    def perform_create(self, serializer: CardSerializer) -> None:
        """
        Called when saving a new object instance. Add the current user
        (based on the token) as the owner of the deck.
        """
        serializer.save(deck=self.deck)

    def get_queryset(self) -> QuerySet:
        """
        Return only the decks owned by the current user (based on the
        token).
        """
        return self.queryset.filter(deck=self.deck)


class CardRetrieveView(generics.RetrieveAPIView):

    queryset = Card.objects.all()
    serializer_class = CardSerializer

    lookup_field = 'id'
