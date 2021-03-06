import copy

FOCUS = 0x0001
PROJECTILE = 0x0002
EFFECT = 0x0004
CREATURE = 0x0008
AUGMENT = 0x0016

FROST = 'Frost'
FIRE = 'Fire'
GLASS = 'Glass'
SILK = 'Silk'
METAL = 'Metal'
LIGHTNING = 'Lightning'
EARTH = 'Earth'
POISON = 'Poison'
ILLUSION = 'Illusion'
BLOOD = 'Blood'

FROZEN = 'frozen'
ENTANGLED = 'entangled'
STUNNED = 'stunned'

class Card(object):

    #Represents a card
    count = 0
    def __init__(self):
        Card.count += 1
        self.id = self.count
        self.virtual = False

    def copy(self):
        copied_card = copy.copy(self)
        copied_card.virtual = True
        copied_card.cardname += ' (virtual)'
        return copied_card
        

    def give_id(self):
        return self.id
        
    def put_out(self, player):
        #Defines what happens when card is put into play
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
        self.blocked = False

    def put_out(self, game, player):
        pass

    def is_blocked(self, player):
        self.blocked = True

    def activate(self, game, player, creature):
        pass

    def when_remove_to_hand(self, game, player):
        pass

    def when_remove_to_discard(self, game, player):
        pass

class Augment(Card):
    cardtype = AUGMENT
    def __init__(self):
        Card.__init__(self)

    def put_out(self, game, player):
        pass

    def activate(self, game, player, projectile):
        pass

    def when_remove_to_hand(self, game, player):
        pass

    def when_remove_to_discard(self, game, player):
        pass

class Creature(Card):
    cardtype = CREATURE
    def __init__(self):
        Card.__init__(self)
        self.conditions = {FROZEN:0,ENTANGLED:0,STUNNED:0}

    def check_conditions(self):
        for x in self.conditions:
            if self.conditions[x] > 0:
                self.conditions[x] -= 1

    def take_condition(self, condition, count):
        self.conditions[condition] = count        

    def put_out(self, game, player):
        pass

    def activate(self, game, player, creature):
        pass

    def block(self, game, player):
        pass

    def when_remove_to_hand(self, game, player):
        pass

    def when_remove_to_discard(self, game, player):
        pass

class Effect(Card):
    cardtype = EFFECT
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
