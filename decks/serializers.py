from rest_framework import serializers
from cards.models import Card
from cards.serializer import CardSerializer

from .models import Deck


class DeckSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()

    class Meta:
        model = Deck
        fields = ('id', 'name', 'cards')

    def get_cards(self, deck):
        """
        Return the serialized json of the cards from the deck.
        """
        cards = Card.objects.filter(deck_id=deck.id)
        return CardSerializer(cards, many=True).data
