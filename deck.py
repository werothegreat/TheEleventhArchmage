from random import shuffle
import card

class Deck(object):
    #Represents a set of cards, whether draw pile, hand, in play, or discard
    def __init__(self):
        self.cards = []

    def add(self, card):
        #puts card on top
        if not card in self.cards:
            self.cards.append(card)

    def remove(self, card):
        #removes a card
        self.cards.remove(card)

    def shuffle_into(self, other_deck):
        #shuffles all cards into other deck
        other_deck.cards.extend(self.cards)
        other_deck.shuffle()
        self.cards = []

    def shuffle(self):
        #shuffles deck
        shuffle(self.cards)
