from deck import Deck
from card import Card, Focus, Projectile, FOCUS, PROJECTILE

class Player(object):

    health = 20
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
        self.health = Player.health

    def move_card_to(self, card, target_deck):
        #Moves card to/from deck, hand, play, discard
        for deck in (self.draw, self.hand, self.inPlay, self.discard):
            if card in deck.cards:
                deck.remove(card)
        target_deck.add(card)

    def put_out_card(self, card):
        if card.cardtype == FOCUS:
            self.move_card_to(card, self.inPlay)
        elif card.cardtype == PROJECTILE:
            if (card.focustype in self.focusTotal) and (self.focusTotal[card.focustype] >= card.focuscost[card.focustype]):
                if card.focustype not in self.usedFocus:
                    self.usedFocus[card.focustype] = card.focuscost[card.focustype]
                else:
                    self.usedFocus[card.focustype] += card.focuscost[card.focustype]
                self.move_card_to(card, self.inPlay)
            else:
                print('You don\'t have enough focus.')
        

    def draw_card(self):
        #Moves card specifically from draw deck to hand
        self.move_card_to(self.draw.top_card(), self.hand)

    def activate_card(self, card):
        #Activates a card during the play phase
        card.activate(game, self)

    def deal_damage_to(self, card, other_player, damage=0):
        attacker = self
        attacking_card = card
        other_player.health -= damage
        
