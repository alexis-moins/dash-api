from rest_framework import generics
from django.db.models import QuerySet

from .models import Card
from .serializer import CardSerializer


class CardListCreateView(generics.ListCreateAPIView):
    """

    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer: CardSerializer) -> None:
        """
        Called when saving a new object instance. Add the current user
        (based on the token) as the owner of the deck.
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self) -> QuerySet:
        """
        Return only the decks owned by the current user (based on the
        token).
        """
        return self.queryset.filter(owner=self.request.user)


class CardRetrieveView(generics.RetrieveAPIView):

    queryset = Card.objects.all()
    serializer_class = CardSerializer

    lookup_field = 'id'
