from random import shuffle

class Deck(object):
    #Represents a set of cards, whether draw pile, hand, in play, or discard
    count = 0
    def __init__(self):
        self.cards = []

    def add(self, card):
        #puts card on top
        if not card in self.cards:
            self.cards.append(card)
            self.count += 1

    def remove(self, card):
        #removes a card
        self.cards.remove(card)
        self.count -= 1

    def shuffle_into(self, other_deck):
        #shuffles all cards into other deck
        other_deck.cards.extend(self.cards)
        other_deck.shuffle()
        other_deck.count += self.count
        self.cards = []
        self.count = 0

    def shuffle(self):
        #shuffles deck
        shuffle(self.cards)

    def length(self):
        #gives size of deck
        return self.count

    def top_card(self):
        #Gives top card
        return self.cards[self.length()-1]
