from card import Card

class PlayerHand():
    """
    >>> card_1 = Card("A", "spades")
    >>> card_2 = Card(2, "diamonds")
    >>> card_3 = Card(3, "clubs")
    >>> card_4 = Card(4, "hearts")
    >>> card_5 = Card(5, "spades")
    >>> card_6 = Card("K", "diamonds")
    >>> card_7 = Card("J", "clubs")
    >>> card_8 = Card("Q", "hearts")
    
    >>> p_hand = PlayerHand()
    >>> p_hand.add_card(card_1, card_2)
    >>> p_hand
    (2, diamonds) (A, spades)
    >>> p_hand.add_card(card_3)
    >>> print(p_hand)
    ____
    |2  |
    | ♦ |
    |__2|
    ____
    |3  |
    | ♣ |
    |__3|
    ____
    |A  |
    | ♠ |
    |__A|
    
    >>> p_hand
    (2, diamonds) (3, clubs) (A, spades)

    >>> d_hand = DealerHand()
    >>> d_hand.add_card(card_4)
    >>> d_hand.add_card(card_5, card_6)
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |?  |
    | ? |
    |__?|
    ____
    |?  |
    | ? |
    |__?|
    >>> d_hand
    (4, hearts) (?, ?) (?, ?)
    >>> d_hand.reveal_hand()
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |5  |
    | ♠ |
    |__5|
    ____
    |K  |
    | ♦ |
    |__K|
    >>> d_hand
    (4, hearts) (5, spades) (K, diamonds)
    """

    #python3 -i hand.py
    #python3 -m doctest hand.py
    
    def __init__(self):
        self.cards = []
        
    def add_card(self, *cards):
        """
        Adds cards to the hand, then sorts
        them in ascending order.
        """
        
        for card in cards:
            assert isinstance(card, Card)
            self.cards.append(card)
        self.sort_hand()

    def get_cards(self):
        return self.cards            

    def __str__(self):
        """
        Returns the string representation of all cards
        in the hand, with each card on a new line.
        """
        string = []
        for i in self.cards:
            string.append(str(i))
        return "\n".join(string)
    
    def __repr__(self):
        """
        Returns the representation of all cards, with 
        each card separated by a space.
        """
        repr_string = []
        for i in self.cards:
            repr_string.append(repr(i))
        return ' '.join(repr_string)

    def sort_hand(self):
        """
        Sorts the cards in ascending order.
        """
        l = len(self.cards)
        for i in range(l):
            for j in range(0, l-i-1):
                if self.cards[j] > self.cards[j+1]:
                    self.cards[j], self.cards[j+1] = self.cards[j+1], self.cards[j]
        
    
class DealerHand(PlayerHand):
    
    def __init__(self):
        # This should inherit attributes from
        # the parent PlayerHand class.
        super(DealerHand, self).__init__()
        self.hand_visible = False

    def add_card(self, *cards):
        """
        Adds the cards to hand such that only the first card
        in the hand is visible (when the dealer's hand is not visible).
        If the dealer's hand is visible, then add cards to hand as 
        usual and sort them in ascending order.
        """
        if self.hand_visible == False:            
            for card in cards:
                assert isinstance(card,Card)
                self.cards.append(card)
            for card in cards:
                if self.cards.index(card) != 0:
                    card.set_visible(False)
        else:
            for card in cards:
                assert isinstance(card, Card)
                self.cards.append(card)
            self.sort_hand()
    
    def reveal_hand(self):
        """
        Makes all the cards in the hand visible
        and sorts them in ascending order.
        """
        for i in self.cards:
            i.set_visible(True)
        self.sort_hand()
        self.hand_visible = True
    
    
    