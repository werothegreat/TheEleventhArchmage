from deck import Deck
from card import * #Card, Focus, Projectile, FOCUS, PROJECTILE, FROST

focus_dict = {FROST:0,FIRE:0,GLASS:0,SILK:0,METAL:0,LIGHTNING:0,EARTH:0,POISON:0,ILLUSION:0,BLOOD:0}

class Player(object):
#Represents player who plays game
    
    count = 0
    health = 20 #this may be altered, potentially
    
    def __init__(self, name, isHuman=True):
        Player.count += 1
        self.id = self.count
        self.name = name
        self.draw = Deck()
        self.hand = Deck()
        self.inPlay = Deck()
        self.discard = Deck()
        self.focusTotal = {FROST:0,FIRE:0,GLASS:0,SILK:0,METAL:0,LIGHTNING:0,EARTH:0,POISON:0,ILLUSION:0,BLOOD:0}
        self.unusedFocus = {FROST:0,FIRE:0,GLASS:0,SILK:0,METAL:0,LIGHTNING:0,EARTH:0,POISON:0,ILLUSION:0,BLOOD:0}
        self.health = Player.health
        self.isHuman = isHuman

    def is_human(self):
        return self.isHuman

    def has_unused_focus(self):
        #Returns whether or not player has focus to use
        for sphere in self.unusedFocus:
            if self.unusedFocus[sphere] > 0:
                hasfocus = True
                break
            else:
                hasfocus = False
        return hasfocus

    def move_card_to(self, card, target_deck):
        #Moves card to/from deck, hand, play, discard
        for deck in (self.draw, self.hand, self.inPlay, self.discard):
            if card in deck.cards:
                deck.remove(card)
        target_deck.add(card)

    def remove_card(self, card):
        #Deletes a card completely
        for deck in (self.draw, self.hand, self.inPlay, self.discard):
            if card in deck.cards:
                deck.remove(card)

    def put_out_card(self, card, target_proj = None):
        #puts a card from your hand into the play area
        if isinstance(card, Focus):
            self.move_card_to(card, self.inPlay)
            card.put_out(self)
            print('{0} has added to their {1} focus.'.format(self.name, card.focustype))
        elif isinstance(card, Projectile) or isinstance(card, Creature):
            if self.unusedFocus[card.focustype] >= card.focuscost[card.focustype]:
                self.move_card_to(card, self.inPlay)
                card.put_out(self)
                print('{0} has put {1} into play.'.format(self.name, card.cardname))
            else:
                print('You don\'t have enough focus.')
        elif isinstance(card, Augment):
            if self.unusedFocus[card.focustype] >= card.focuscost[card.focustype]:
                self.move_card_to(card, self.inPlay)
                card.put_out(self, target_proj)
                print('{0} has put {1} into play, augmenting {2}.'.format(self.name, card.cardname, target_proj.cardname))
            else:
                print('You don\'t have enough focus.')

    def have_inhand(self, cardtype):
        #Sees if a particular card type is in the player's hand
        if self.hand.length() > 0:
            for x in range(self.hand.length()):
                if isinstance(self.hand.cards[x], cardtype):
                    have_it = True
                    break
                else:
                    have_it = False
        else:
            have_it = False
        return have_it

    def lowest_cost_inhand(self, focustype, *cardtype):
        #returns the focus cost of the card with the lowest focus cost in your hand
        oftype = []
        for x in range(self.hand.length()):
            for types in cardtype:
                if isinstance(self.hand.cards[x], types):
                    oftype.append(self.hand.cards[x].focuscost[focustype])
        return min(oftype)    
                    

    def draw_card(self, count=1):
        #Moves card specifically from draw deck to hand
        for x in range(count):
            self.move_card_to(self.draw.top_card(), self.hand)

    def activate_card(self, card, target_player=None, creature=None):
        #Activates a card during the play phase
        if target_player and creature:
            card.activate(self, target_player, creature)
        elif target_player:
            card.activate(self, target_player)
        else:
            card.activate(self)

    '''def activate_all_cards(self):
        for x in range(self.inPlay.length()):
            if not isinstance(self.inPlay.cards[x], Focus):
                has_attack = True
                break
            else:
                has_attack = False
        while has_attack == True:
            for x in range(self.inPlay.length()):
                if self.inPlay.cards[x]'''
            #unfinished

    def have_inplay(self, cardtype):
        #Sees if a particular card type is in the player's hand
        if self.inPlay.length() > 0:
            for x in range(self.inPlay.length()):
                if isinstance(self.inPlay.cards[x], cardtype):
                    have_it = True
                    break
                else:
                    have_it = False
        else:
            have_it = False
        return have_it

    def have_creature_inplay(self):
        if self.inPlay.length() > 0:
            for x in range(self.inPlay.length()):
                if isinstance(self.inPlay.cards[x], Creature):
                    have_creature = True
                    break
                else:
                    have_creature = False
        else:
            have_creature = False
        return have_creature

    def have_proj_inplay(self):
        if self.inPlay.length() > 0:
            for x in range(self.inPlay.length()):
                if isinstance(self.inPlay.cards[x], Projectile) and self.inPlay.cards[x].virtual == False:
                    have_proj = True
                    break
                else:
                    have_proj = False
        else:
            have_proj = False
        return have_proj

    def deal_damage_to(self, card, target_player, damage, creature=None):
        #called by cards in their 'activate' methods to damage other players
        attacker = self
        attacking_card = card
        if creature:
            creature.health -= damage
            print('{0} did {1} damage to {2}\'s {3}!'.format(card.cardname, str(damage), target_player.name, creature.cardname))
            if creature.health <= 0:
                print('{0}\'s {1} has died!'.format(target_player.name, creature.cardname))
                creature.die(target_player)
        else:
            target_player.health -= damage
            print('{0} did {1} damage to {2}!'.format(card.cardname, str(damage), target_player.name))  

    def end_game_cleanup(self):
        #resets your focus and health
        self.hand.shuffle_into(self.draw)
        self.inPlay.shuffle_into(self.draw)
        for sphere in self.focusTotal:
            self.focusTotal[sphere] = 0
        for sphere in self.unusedFocus:
            self.unusedFocus[sphere] = 0
        self.discard.shuffle_into(self.draw)
        self.health = Player.health
                
