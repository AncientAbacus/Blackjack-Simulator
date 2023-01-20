from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)
    """

    #python3 -i deck.py
    #python3 -m doctest deck.py

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        suits = ["clubs", "diamonds", "hearts", "spades"]
        ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.cards = [Card(j, i) for i in suits for j in ranks]
        self.cards.sort()

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all(i == 'modified_overhand' or \
        i == 'mongean' for i in shuffle_and_count)
        assert all(isinstance(i, int) for i in \
        list(shuffle_and_count.values()))

        for arg in shuffle_and_count:
            if arg == 'modified_overhand':
                self.cards = Shuffle.modified_overhand(self.cards, \
                    shuffle_and_count[arg])
            if arg == 'mongean':
                for i in range(shuffle_and_count[arg]):
                    self.cards = Shuffle.mongean(self.cards)

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, PlayerHand)
        hand.add_card(self.cards.pop(0))

    def get_cards(self):
        return self.cards
        
