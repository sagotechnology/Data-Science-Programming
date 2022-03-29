import random

class PlayingCard():
    """This is a class for a single card""" 
    
    def __init__(self, rank="Joker", suit="Joker"):
        self.ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.suits = ["♠", "♥", "♦", "♣"]
    
        if rank not in self.ranks:
            print("Invalid rank!")
            return 
        if suit not in self.suits:
            print("Invalid suit!")
            return
        
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return (self.rank + ' of ' + str(self.suit))
    
class Deck():
    """This class is the deck of cards""" 
    
    def __init__(self, suits=["♠", "♥", "♦", "♣"]):
        Nums=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        
        # create 13 card object per suit and load them into the deck
        self.cards=[]
        for Nm in Nums:
            for s in suits:
                self.cards.append(PlayingCard(rank=Nm, suit=s)) 
        self.shuffle_deck()
        
    def shuffle_deck(self):
        random.shuffle(self.cards) # works in place       
        
    def deal_card(self, card_count):
        if len(self.cards) < card_count:
            print("Cannot deal %d cards. The deck only has %d cards left!" % (card_count, len(self.cards)))
            return None
        dealt = [(self.cards[i].rank, self.cards[i].suit) for i in range(card_count)]
        self.cards = self.cards[card_count:]
        return dealt