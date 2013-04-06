import copy

FOCUS = 0x0001
PROJECTILE = 0x0002
EFFECT = 0x0004
CREATURE = 0x0008

FROST = 'frost'
FIRE = 'fire'
GLASS = 'glass'
SILK = 'silk'
METAL = 'metal'
LIGHTNING = 'lightning'
EARTH = 'earth'
POISON = 'poison'
ILLUSION = 'illusion'
BLOOD = 'blood'

class Card(object):

    #Represents a card
    count = 0
    def __init__(self):
        Card.count += 1
        self.id = self.count

    def give_id(self):
        return self.id
        
    def put_out(self, gplayer):
        #Defines what happens when card is put into play
        pass

    def activate(self, player):
        #Defines what happens when the card is activated during player's turn
        #or another player's turn
        pass

    def when_remove_to_hand(self, player):
        #Defines what happens when the card is removed from play to hand
        pass

    def when_remove_to_discard(self, player):
        #Defines what happens when the card is removed from play to discard
        pass

class Focus(Card):
    cardtype = FOCUS
    def __init__(self):
        Card.__init__(self)

    def put_out(self, game, player):
        pass

    def when_remove_to_hand(self, game, player):
        pass

    def when_remove_to_discard(self, game, player):
        pass

class Projectile(Card):
    cardtype = PROJECTILE
    def __init__(self):
        Card.__init__(self)

    def put_out(self, game, player):
        pass

    def activate(self, game, player):
        pass

    def when_remove_to_hand(self, game, player):
        pass

    def when_remove_to_discard(self, game, player):
        pass

