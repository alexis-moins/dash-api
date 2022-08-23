from rest_framework import generics

from .models import Deck
from .serializers import DeckSerializer


# Each view's `authentication_classes` and `permission_classes` are defined as default
# in the project's settings.py file

class DeckListCreateView(generics.ListCreateAPIView):
    """
    Class-based view to handle POST requests for a single deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class DeckRetrieveView(generics.RetrieveAPIView):
    """
    Class-based view to handle GET requests for a single deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # Which key of the object will be used to retrieve the object
    lookup_field = 'id'


class DeckUpdateView(generics.UpdateAPIView):
    """
    Class-based view to handle PUT requests for a single deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # Which key of the object will be used to retrieve the object
    lookup_field = 'id'


class DeckDeleteView(generics.DestroyAPIView):
    """
    Class-based view to handle DELETE requests for a single deck.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # Which key of the object will be used to retrieve the object
    lookup_field = 'id'
