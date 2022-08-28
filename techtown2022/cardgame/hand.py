from typing import List

from .card import Suit, Card


class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards


class IsFlushMixin:
    def is_flush(self):
        return len(set(card.suit for card in self.cards)) == 1


class PokerHand(Hand, IsFlushMixin):
    ...


class FlushGameHand(Hand, IsFlushMixin):
    ...