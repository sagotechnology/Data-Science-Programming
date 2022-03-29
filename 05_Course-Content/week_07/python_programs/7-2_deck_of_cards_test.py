import random

class PlayingCard():
    
    '''
    Attributes:
    rank
    suit'''
    
    def __init__(self, rank = 'None', suit = 'None'): # allows the class to be it's own instance
        self.rank_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.suit_list = ["♠", "♥", "♦", "♣"]
        if rank not in self.rank_list:
            raise Exception("Invalid rank.")
        self.rank = rank
        if suit not in self.suit_list:
            raise Exception("Invalid suit.")
        self.suit = suit
    
    def __repr__(self):
        return '{self.rank} of {self.suit}'.format(self = self)
    
class Deck():
    """
    Attributes:
    cards"""
    
    def __init__ (self, suit = None):
        rank_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        suit_list = ["♠", "♥", "♦", "♣"]
        self.cards = []
        if suit == None:
            for r in rank_list:
                for s in suit_list:
                    self.cards.append(PlayingCard(rank = r, suit = s))
        else:
            for r in rank_list:
                self.cards.append(PlayingCard(rank = r, suit = suit))
            
    def __repr__(self):
        for card in self.cards:
            print(card)
                    
    def shuffle_deck(self):
        random.shuffle(self.cards)
        
    def deal_card(self, card_count):
        if card_count > len(self.cards):
            raise Exception("Cannot deal " + str(card_count) + " cards. The deck \
only has " + str(len(self.cards)) + " cards left!")
        else:
            i = 0
            deal = []
            while i < card_count:
                deal.append(self.cards.pop(0))
                i += 1
            return deal
