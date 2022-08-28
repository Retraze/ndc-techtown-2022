# add a shuffle init arg, use random module
import random
# construct a list of cards using itertools
import itertools

# learn: relative imports
from .card import Card


class DeckEmptyError(Exception):
    ...


class Deck:
    def __init__(self, shuffle=False):
        self.cards = list(Card.from_tuple(t) for t in itertools.product(range(2,15),"CDHS"))
        if shuffle:
            random.shuffle(self.cards)

    def draw(self, numcards=1):
        if numcards > len(self.cards):
            raise DeckEmptyError()
        drawed, self.cards = self.cards[:numcards], self.cards[numcards:]
        return drawed
