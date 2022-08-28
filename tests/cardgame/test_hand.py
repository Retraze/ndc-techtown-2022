from techtown2022.cardgame.card import Card
from techtown2022.cardgame.hand import PokerHand


def test_pokerhand_flush():
    cards = [Card.from_str(s) for s in ["2H", "3H", "4H", "5H", "6H"]]
    poker_hand = PokerHand(cards)
    assert poker_hand.is_flush()


def test_pokerhand_not_flush():
    cards = [Card.from_str(s) for s in ["2H", "3C", "4D", "5S", "6H"]]
    poker_hand = PokerHand(cards)
    assert not poker_hand.is_flush()