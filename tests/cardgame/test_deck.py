from python_properly.cardgame.deck import Deck


unshuffled_order = [
        (0, "2 of Clubs"),
        (1, "2 of Diamonds"),
        (2, "2 of Hearts"),
        (3, "2 of Spades"),
        (-2, "Ace of Hearts"),
        (-1, "Ace of Spades"),
    ]

def test_deck():
    deck = Deck()
    cards = deck.cards
    assert len(cards) == 52
    for i, s in unshuffled_order:
        assert str(cards[i]) == s


def test_deck_shuffle():
    deck1 = Deck(shuffle=True)
    assert len(deck1.cards) == 52
    
    deck2 = Deck(shuffle=True)
    # we are checking that the ordering are not identical between two shuffled decks
    # this assertion might incorrectly fail, but with very low likelihood
    assert not all(a.rank==b.rank and a.suit == b.suit for a, b in zip(deck1.cards, deck2.cards))


def test_deck_draw():
    deck = Deck()
    five_cards = deck.draw(5)
    assert len(five_cards) == 5
    assert len(deck.cards) == 52-5

    assert [str(card) for card in five_cards] == [
        "2 of Clubs",
        "2 of Diamonds",
        "2 of Hearts",
        "2 of Spades",
        "3 of Clubs",
    ]
