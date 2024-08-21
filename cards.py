import random

class Card:
    def __init__(self, character, suit, value):
        self.character = character
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.character} - {self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = [["A","Spades"], ["B","Hearts"], ["C","Diamonds"], ["D","Clubs"]]
        values = [["1","Ace"],["2","2"],["3","3"],["4","4"],["5","5"],["6","6"],["7","7"],["8","8"],["9","9"],["A","10"],["B","Jack"],["D","Queen"],["E","King"]]

        for suit in suits:
            for value in values:
                self.cards.append(Card(chr(int(f"1F0{suit[0]}{value[0]}", 16)) , suit[1], value[1]))

        random.shuffle(self.cards)  # Shuffle the deck
    def deal(self):
        if self.cards:
            return self.cards.pop(0)  # Remove and return the first card
        else:
            return "No more cards in the deck!"
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
