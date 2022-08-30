from rest_framework import generics
from django.db.models import QuerySet

from .models import Deck
from .permissions import IsDeckOwner
from .serializers import DeckSerializer


# Each view's `authentication_classes` and `permission_classes` are defined as default
# in the project's settings.py file
class DeckListCreateView(generics.ListCreateAPIView):
    """
    Class-based view to list the deck collection of the current user
    or to create a new deck for the current user.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def perform_create(self, serializer: DeckSerializer) -> None:
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


class DeckRetrieveView(generics.RetrieveAPIView):
    """
    Class-based view to handle GET requests for a single deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # Only show the deck's info if the user is the owner
    permission_classes = [IsDeckOwner]

    # Which key of the object will be used to retrieve the object
    lookup_field = 'id'


class DeckUpdateView(generics.UpdateAPIView):
    """
    Class-based view to handle PUT requests for a single deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # Only delete the deck if the user is the owner
    permission_classes = [IsDeckOwner]

    # Which key of the object will be used to retrieve the object
    lookup_field = 'id'


class DeckDeleteView(generics.DestroyAPIView):
    """
    Class-based view to handle DELETE requests for a single deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # Only delete the deck if the user is the owner
    permission_classes = [IsDeckOwner]

    # Which key of the object will be used to retrieve the object
    lookup_field = 'id'
