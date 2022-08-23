# add a shuffle init arg, use random module
import random
# construct a list of cards using itertools
import itertools

# learn: relative imports
from .card import Card

class Deck:
    def __init__(self, shuffle=False):
        self.cards = list(Card.from_tuple(t) for t in itertools.product(range(2,15),"SHDC"))
        if shuffle:
            random.shuffle(self.cards)