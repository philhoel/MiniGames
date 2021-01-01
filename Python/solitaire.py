import numpy as np
import random

class Card:

    def __init__(self, t, v):
        self.type = t
        self.val = v

    def show(self):
        print(f"{self.type} {self.val}")

class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for t in ["Spades", "Clover", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(t, v))

    def suffleDeck(self):
        random.shuffle(self.cards)
        

class Board:

    def __init__(self):
        self.cardsOnScreen = []
