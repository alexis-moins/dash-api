from rest_framework.decorators import api_view
from rest_framework.response import Response

from decks.serializers import DeckSerializer
from decks.models import Deck


@api_view(['GET'])
def get_decks(_):
    """
    Return the list of decks in the database.

    Return value:
    A list of decks
    """
    decks = Deck.objects.all()
    data = [DeckSerializer(deck).data for deck in decks] if decks else {}

    return Response(data)


@api_view(['POST'])
def create_deck(request):
    """
    Create a new deck and commit it into the database.

    Return value:
    The data of the newly created Deck
    """
    serializer = DeckSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
