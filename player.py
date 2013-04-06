from deck import Deck
from card import Card, Focus, Projectile, FOCUS, PROJECTILE, FROST

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
        self.focusTotal = {FROST:0}
        self.unusedFocus = {FROST:0}
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
            card.put_out(self)
            print('You have added to your {0} focus.'.format(card.focustype))
        elif card.cardtype == PROJECTILE:
            if (card.focustype in self.focusTotal) and (self.unusedFocus[card.focustype] >= card.focuscost[card.focustype]):
                self.unusedFocus[card.focustype] -= card.focuscost[card.focustype]
                self.move_card_to(card, self.inPlay)
                print('You have put {0} into play.'.format(card.cardname))
            else:
                print('You don\'t have enough focus.')
        

    def draw_card(self):
        #Moves card specifically from draw deck to hand
        self.move_card_to(self.draw.top_card(), self.hand)

    def activate_card(self, card, target_player):
        #Activates a card during the play phase
        card.activate(self, target_player)
        self.move_card_to(card, self.discard)
        self.unusedFocus[card.focustype] += card.focuscost[card.focustype]

    def deal_damage_to(self, card, other_player, damage=0):
        attacker = self
        attacking_card = card
        other_player.health -= damage
        print('{0} did {1} damage to {2}!'.format(card.cardname, str(damage), other_player.name))
        
