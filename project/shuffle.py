class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    """    

    #python3 -i shuffle.py
    #python3 -m doctest shuffle.py
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        
        assert isinstance(cards, list)
        assert isinstance(num, int)

        mid = len(cards) // 2

        if num == 0:
            return cards
        else:
            if len(cards)%2 == 0 and num%2 == 1:
                top, bottom = ((mid - (num // 2)) - 1), (mid + (num // 2))
            elif len(cards)%2 == 1 and num %2 == 0:
                top, bottom = ((mid - (num // 2))), (mid + (num // 2))
            else:
                if len(cards) % 2 == 0 and num % 2 == 0:
                    top, bottom = mid - num//2, mid + num//2
                if len(cards) % 2 == 1 and num % 2 == 1:
                    top, bottom = mid - num//2, mid + num//2 + 1

            to_insert = cards[top:bottom]
            del cards[top:bottom]
            
            for i in reversed(to_insert):
                cards.insert(0, i)

            return Shuffle.modified_overhand(cards, num - 1)
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        cards_2 = []

        def inner(cards):
            if len(cards) == 0:
                return cards_2
            if len(cards) % 2 == 0:
                cards_2.append(cards[0])
            else:
                cards_2.insert(0, cards[0])
            return inner(cards[1:])

        if len(cards)%2!=0:
            return list(reversed(inner(cards)))
        else:
            return inner(cards)





    