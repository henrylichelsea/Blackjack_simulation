import numpy as np
import pandas as pd
import random
import deck

# Six deck games
six_deck = deck.Deck(6)
six_deck.shuffle()
six_deck.show()
six_deck.countCard()

# Create one-vs-one battle between dealer and me
Henry = deck.Player('Henry')
Dealer = deck.Player('Dealer')

# Create

