from enum import Enum

# learn: union type
from typing import Union

# learn: custom exceptions
class InvalidCardError(Exception):
    ...


# learn: custom exceptions with __init__ and __str__ override
class InvalidRankError(InvalidCardError):
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return f"{self.rank} is not a valid rank. Must be int type between 2-14"


class InvalidSuitError(InvalidCardError):
    def __init__(self, suit):
        self.suit = suit

    def __str__(self):
        return f"{self.suit} is not a valid suit. Must be a valid Suit type"


# learn: Enum
class Suit(Enum):
    Spades = "S"
    Hearts = "H"
    Diamonds = "D"
    Clubs = "C"

    @classmethod
    def from_str(cls, suit: str):
        if type(suit) != str:
            raise InvalidSuitError(suit)
        try:
            return cls[suit]
        except KeyError:
            pass
        try:
            return cls(suit)
        except ValueError:
            raise InvalidSuitError(suit)


class Card:
    # learn: class attributes
    rank_mapping = {11: "Knight", 12: "Queen", 13: "King", 14: "Ace"}
    suit_ascending_values = [
        Suit.Clubs,
        Suit.Diamonds,
        Suit.Hearts,
        Suit.Spades,
    ]

    # learn: type hinting
    def __init__(self, rank: int, suit: Union[Suit, str]):
        if not self.is_valid_rank(rank):
            raise InvalidRankError(rank)
        self.rank = rank

        self.suit = suit if type(suit) is Suit else Suit.from_str(suit)

    # learn: classmethod
    @classmethod
    def from_tuple(cls, t):
        if len(t) not in [2, 3]:
            raise InvalidCardError(f"{s} is not a valid input string")
        # unpacking
        return cls(*t)

    @classmethod
    def from_str(cls, s):
        if len(s) not in [2, 3]:
            raise InvalidCardError(f"{s} is not a valid input string")

        rank = s[:-1]
        try:
            rank = int(rank)
        except ValueError:
            # should we raise InvalidRank, or perhaps InvalidCardError from InvalidRank?
            raise InvalidRankError(s)

        try:
            suit = Suit(s[-1])
        except ValueError:
            raise InvalidSuitError(s)

        return cls(rank, suit)

    # learn: property
    @property
    def rank_str(self):
        return str(self.rank_mapping.get(self.rank, self.rank))

    # learn: staticmethod
    @staticmethod
    def is_valid_rank(rank: int):
        return type(rank) is int and rank >= 2 and rank <= 14

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        if self.rank == other.rank:
            if self.suit_ascending_values.index(self.suit) < self.suit_ascending_values.index(other.suit):
                return True
        return False

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    # learn: __str__
    def __str__(self):
        return f"{self.rank_str} of {self.suit.name}"

    # learn: __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}<{self.rank}{self.suit.value}>"
