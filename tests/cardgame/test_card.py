import pytest
import inspect

from techtown2022.cardgame.card import Card, Suit, InvalidCardError, InvalidRankError, InvalidSuitError


def test_suit_from_name():
    Suit["Hearts"]
    Suit["Spades"]
    Suit["Diamonds"]
    Suit["Clubs"]
    assert len(Suit.__members__) == 4


def test_invalid_suit_from_name():
    with pytest.raises(KeyError):
        Suit["Scades"]


def test_suit_from_value():
    Suit("H")
    Suit("S")
    Suit("D")
    Suit("C")


def test_invalid_suit_from_value():
    with pytest.raises(ValueError):
        Suit("A")


def test_card_suit_enum():
    card = Card(3, Suit.Spades)
    assert card.rank == 3
    assert card.suit == Suit.Spades


def test_card_invalid_rank():
    invalid_ranks = [-3, 0, 1, 15, "4"]
    for rank in invalid_ranks:
        with pytest.raises(InvalidRankError):
            Card(rank, Suit.Spades)


def test_suit_from_string():
    assert Suit.from_str("Spades") == Suit.Spades
    assert Suit.from_str("H") == Suit.Hearts

    with  pytest.raises(InvalidSuitError):
        Suit.from_str("HH")
    with  pytest.raises(InvalidSuitError):
        Suit.from_str("Blubs")


def test_card_invalid_suit_type():
    invalid_suits = [-3, [], None]
    for suit in invalid_suits:
        with pytest.raises(InvalidSuitError):
            Card(2, suit)

def test_card_invalid_suit_str():
    with pytest.raises(InvalidSuitError):
        Card(2, "Heartz")


def test_card_suit_str_name():
    card = Card(3, "Spades")
    assert card.rank == 3
    assert card.suit == Suit.Spades


def test_card_suit_str_value():
    card = Card(3, "S")
    assert card.rank == 3
    assert card.suit == Suit.Spades


def test_card_str():
    assert str(Card(14, Suit.Spades)) == "Ace of Spades"
    assert str(Card(6, Suit.Diamonds)) == "6 of Diamonds"


def test_card_repr():
    assert repr(Card(12, Suit.Clubs)) == "Card<12C>"


def test_rank_str_property():
    card = Card(14, Suit.Clubs)
    assert card.rank_str == "Ace"

    card = Card(7, Suit.Spades)
    assert card.rank_str == "7"

def test_card_sort():
    cards = [
        Card(14, Suit.Clubs),
        Card(14, Suit.Diamonds),
        Card(14, Suit.Spades),
        Card(14, Suit.Hearts),
        Card(5, Suit.Clubs),
        Card(10, Suit.Clubs),
    ]
    cards.sort()
    assert cards == [
        Card(5, Suit.Clubs),
        Card(10, Suit.Clubs),
        Card(14, Suit.Clubs),
        Card(14, Suit.Diamonds),
        Card(14, Suit.Hearts),
        Card(14, Suit.Spades),
    ]

"""
def test_suit_sort():
    suits = [
        Suit.Clubs,
        Suit.Diamonds,
        Suit.Spades,
        Suit.Hearts,
        Suit.Clubs,
        Suit.Clubs,
    ]
    suits.sort()
    assert suits == [
        Suit.Clubs,
        Suit.Clubs,
        Suit.Clubs,
        Suit.Diamonds,
        Suit.Hearts,
        Suit.Spades,
    ]
"""

def test_from_str():
    card = Card.from_str("13D")
    assert card.rank == 13
    assert card.suit == Suit.Diamonds

    first_arg = inspect.getfullargspec(Card.from_str)[0][0]
    assert first_arg != "self", "classmethod should not have `self` (instance) as first argument. Use `cls` (class) instead"


def test_from_str_invalid():
    invalid_from_str = ["1H", "-1D", "130S", "4B"]
    for s in invalid_from_str:
        with pytest.raises(InvalidCardError):
            Card.from_str(s)


#def test_from_tuple():
#    raise NotImplementedError


if __name__ == '__main__':
    pytest.main(args=[__file__])