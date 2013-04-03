from deck import Deck

class Player(object):

    health = 50
    #Represents player who plays game
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.draw = Deck()
        self.hand = Deck()
        self.inPlay = Deck()
        self.discard = Deck()
        self.focusTotal = {}
        self.usedFocus = {}

    def move_card_to(self, card, target_deck):
        #Moves card to/from deck, hand, play, discard
        for deck in (self.draw, self.hand, self.inPlay, self.discard):
            if card in deck:
                deck.remove(card)
        target_deck.add(card)
