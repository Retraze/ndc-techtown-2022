# learn: __init__.py and __all__ ?
# from python_properly.cardgame import Deck
from python_properly.cardgame.deck import Deck


unshuffled_order = [
        (0, "2 of Spades"),
        (1, "2 of Hearts"),
        (2, "2 of Diamonds"),
        (3, "2 of Clubs"),
        (-2, "Ace of Diamonds"),
        (-1, "Ace of Clubs"),
    ]

def test_card():
    deck = Deck()
    cards = deck.cards
    assert len(cards) == 52
    for i, s in unshuffled_order:
        assert str(cards[i]) == s


def test_card_shuffle():
    deck1 = Deck(shuffle=True)
    assert len(deck1.cards) == 52
    
    deck2 = Deck(shuffle=True)
    # we are checking that the ordering are not identical between two shuffled decks
    # this assertion might incorrectly fail, but with very low likelihood
    assert not all(a.rank==b.rank and a.suit == b.suit for a, b in zip(deck1.cards, deck2.cards))

