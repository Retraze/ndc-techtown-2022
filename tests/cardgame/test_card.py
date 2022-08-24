import pytest
import inspect

from python_properly.cardgame.card import Card, Suit, InvalidCard, InvalidRank, InvalidSuit


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
        # TODO: should we assert something about str(InvalidRank) ?
        with pytest.raises(InvalidRank):
            card = Card(rank, Suit.Spades)


def test_card_invalid_suit_str():
    with pytest.raises(InvalidSuit):
        card = Card(2, "Heartz")


def test_card_invalid_suit_type():
    invalid_suits = [-3, [], None]
    for suit in invalid_suits:
        with pytest.raises(InvalidCard):
            card = Card(2, suit)


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


def test_card_repr():
    assert repr(Card(12, Suit.Clubs)) == "Card<12C>"


def test_from_str():
    card = Card.from_str("13D")
    assert card.rank == 13
    assert card.suit == Suit.Diamonds

    first_arg = inspect.getfullargspec(Card.from_str)[0][0]
    assert first_arg != "self", "classmethod should not have `self` (instance) as first argument. Use `cls` (class) instead"