from deck import Deck
from card import * #Card, Focus, Projectile, FOCUS, PROJECTILE, FROST

focus_dict = {FROST:0,FIRE:0,GLASS:0,SILK:0,METAL:0,LIGHTNING:0,EARTH:0,POISON:0,ILLUSION:0,BLOOD:0}

class Player(object):
#Represents player who plays game
    
    count = 0
    health = 20 #this may be altered, potentially
    
    def __init__(self, name, game):
        Player.count += 1
        self.id = self.count
        self.name = name
        self.game = game
        self.draw = Deck()
        self.hand = Deck()
        self.inPlay = Deck()
        self.discard = Deck()
        self.focusTotal = {FROST:0,FIRE:0,GLASS:0,SILK:0,METAL:0,LIGHTNING:0,EARTH:0,POISON:0,ILLUSION:0,BLOOD:0}
        self.unusedFocus = {FROST:0,FIRE:0,GLASS:0,SILK:0,METAL:0,LIGHTNING:0,EARTH:0,POISON:0,ILLUSION:0,BLOOD:0}
        self.health = Player.health

    def move_card_to(self, card, target_deck):
        #Moves card to/from deck, hand, play, discard
        for deck in (self.draw, self.hand, self.inPlay, self.discard):
            if card in deck.cards:
                deck.remove(card)
        target_deck.add(card)

    def put_out_card(self, card):
        #puts a card from your hand into the play area
        if card.cardtype == FOCUS:
            self.move_card_to(card, self.inPlay)
            card.put_out(self)
            print('{0} has added to their {1} focus.'.format(self.name, card.focustype))
        elif card.cardtype == PROJECTILE:
            if (card.focustype in self.focusTotal) and (self.unusedFocus[card.focustype] >= card.focuscost[card.focustype]):
                self.unusedFocus[card.focustype] -= card.focuscost[card.focustype]
                self.move_card_to(card, self.inPlay)
                print('{0} has put {1} into play.'.format(self.name, card.cardname))
            else:
                print('You don\'t have enough focus.')

    def have_focus_inhand(self):
        #boolean - do you have a focus in hand?
        if self.hand.length() > 0:
            for x in range(self.hand.length()):
                if self.hand.cards[x].cardtype == FOCUS:
                    have_focus = True
                    break
                else:
                    have_focus = False
        else:
            have_focus = False
        return have_focus
        
    def have_nonfocus_inhand(self):
        #boolean value - is there a non-focus card in your hand?
        if self.hand.length() > 0:
            for x in range(self.hand.length()):
                if self.hand.cards[x].cardtype != FOCUS:
                    have_nonfocus = True
                    break
                else:
                    have_nonfocus = False
        else:
            have_nonfocus = False
        return have_nonfocus

    def lowest_cost_inhand(self, focustype):
        #returns the focus cost of the card with the lowest focus cost in your hand
        nonfocuses = []
        for x in range(self.hand.length()):
            if self.hand.cards[x].cardtype != FOCUS:
                nonfocuses.append(self.hand.cards[x].focuscost[focustype])
        return min(nonfocuses)    
                    

    def draw_card(self, count=1):
        #Moves card specifically from draw deck to hand
        for x in range(count):
            self.move_card_to(self.draw.top_card(), self.hand)

    def activate_card(self, card, target_player):
        #Activates a card during the play phase
        card.activate(self, target_player)
        self.move_card_to(card, self.discard)
        self.unusedFocus[card.focustype] += card.focuscost[card.focustype]

    def deal_damage_to(self, card, other_player, damage=0):
        #called by cards in their 'activate' methods to damage other players
        attacker = self
        attacking_card = card
        other_player.health -= damage
        print('{0} did {1} damage to {2}!'.format(card.cardname, str(damage), other_player.name))
        
