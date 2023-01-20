class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    #python3 -i card.py
    #python3 -m doctest card.py


    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert isinstance(rank, str) or isinstance(rank, int)
        assert isinstance(suit, str)
        assert isinstance(visible, bool)
        self.rank = rank 
        self.suit = suit 
        self.visible = visible
        

    def __lt__(self, other_card):
        suits = ["clubs", "diamonds", "hearts", "spades"]
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        if ranks.index(self.rank) == ranks.index(other_card.rank):
            if suits.index(self.suit) < suits.index(other_card.suit):
                return True
        if ranks.index(self.rank) < ranks.index(other_card.rank):
            return True
        else:
            return False



    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if self.visible == False:
            return "____\n" + \
            "|" + '?' + "  |\n" + \
            "| " + '?' + " |\n" + \
            "|__" + '?' + "|" 
        else:
            if self.suit == "hearts":
                return "____\n" + \
                "|" + str(self.rank) + "  |\n" + \
                "| " + "♥" + " |\n" + \
                "|__" + str(self.rank) + "|"
            if self.suit == "spades":
                return "____\n" + \
                "|" + str(self.rank) + "  |\n" + \
                "| " + "♠" + " |\n" + \
                "|__" + str(self.rank) + "|" 
            if self.suit == "clubs":
                return "____\n" + \
                "|" + str(self.rank) + "  |\n" + \
                "| " + "♣" + " |\n" + \
                "|__" + str(self.rank) + "|" 
            if self.suit == "diamonds":
                return "____\n" + \
                "|" + str(self.rank) + "  |\n" + \
                "| " + "♦" + " |\n" + \
                "|__" + str(self.rank) + "|" 

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """        

        if self.visible == True:
            return "(" + str(self.rank) + ", " + str(self.suit) + ")"
        else:
            return "(?, ?)"

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
    