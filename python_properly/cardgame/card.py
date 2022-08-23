from enum import Enum

# union type
from typing import Union

# custom exception
class InvalidCard(Exception):
    ...


class InvalidRank(InvalidCard):
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return f"{self.rank} is not a valid rank. Must be int type between 2-14"


class InvalidSuit(InvalidCard):
    def __init__(self, suit):
        self.suit = suit

    def __str__(self):
        return f"{self.suit} is not a valid suit. Must be a valid Suit type"


class Suit(Enum):
    Spades = "S"
    Hearts = "H"
    Diamonds = "D"
    Clubs = "C"


class Card:
    rank_mapping = {11: "Knight", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, rank: int, suit: Union[Suit, str]):
        if not self.is_valid_rank(rank):
            raise InvalidRank(rank)
            # alternatively:
            # raise InvalidCard(f"{rank} is not a valid rank") from InvalidRank(rank)
        self.rank = rank

        self.suit = suit if type(suit) is Suit else self.parse_suit(suit)

    @classmethod
    def from_tuple(cls, t):
        if len(t) not in [2, 3]:
            raise InvalidCard(f"{s} is not a valid input string")
        # unpacking
        return cls(*t)

    @classmethod
    def from_str(cls, s):
        if len(s) not in [2, 3]:
            raise InvalidCard(f"{s} is not a valid input string")
        try:
            rank = int(s[:-1])
        except ValueError:
            # should we raise InvalidRank, or perhaps InvalidCard from InvalidRank?
            raise InvalidCard(f"{s} is not a valid rank")
        try:
            suit = Suit(s[-1])
        except ValueError:
            raise InvalidCard(f"{s} is not a valid suit")

        return cls(rank, suit)

    @property
    def rank_str(self):
        return str(self.rank_mapping.get(self.rank, self.rank))

    @staticmethod
    def is_valid_rank(rank: int):
        return type(rank) is int and rank >= 2 and rank <= 14

    @staticmethod
    def parse_suit(suit: str):
        if type(suit) != str:
            raise InvalidSuit(suit)
        try:
            return Suit[suit]
        except KeyError:
            pass
        try:
            return Suit(suit)
        except ValueError:
            raise InvalidSuit(suit)

    def __str__(self):
        return f"{self.rank_str} of {self.suit.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}<{self.rank}{self.suit.value}>"
