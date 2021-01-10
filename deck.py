import random
import numpy as np

class Card:
    
    def __init__(self, value, suit):
        self.value = value 
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:

    def __init__(self, num_of_deck):
        self.cards = []
        self.num_of_deck = num_of_deck
        self.build()

    def build(self):
        counter = 0
        while counter < self.num_of_deck:
            for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
                for v in range(1, 14):
                    self.cards.append(Card(v, s))
            counter += 1
        
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def drawcard(self):
        return self.cards.pop()

    def countCard(self):
        print(len(self.cards))

    
class Player:
    
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawcard())
    
    def showHand(self):
        for card in self.hand:
            card.show()
