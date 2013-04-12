from card import * #Card, Focus, Projectile, EFFECT, CREATURE, FROST
from player import Player

class FrostRing(Focus):

    cardname = 'Frost Ring'
    focustype = FROST
    text = 'Provides 1 Frost focus.'
    

    def __init__(self):
        Card.__init__(self)

    def put_out(self, player):
        player.focusTotal[FROST] += 1
        player.unusedFocus[FROST] += 1

    def when_remove_to_hand(self, player):
        player.focusTotal[FROST] -= 1
        player.unusedFocus[FROST] -= 1

    def when_remove_to_discard(self, player):
        player.focusTotal[FROST] -= 1
        player.unusedFocus[FROST] -= 1

    def when_remove_from_play(self, player):
        player.focusTotal[FROST] -= 1
        player.unusedFocus[FROST] -= 1

class Icicle(Projectile):

    cardname = 'Icicle'
    focustype = FROST
    focuscost = {FROST : 1}
    damage = 2
    text = 'Deals 2 damage to target player or creature.'

    def __init__(self):
        Projectile.__init__(self)

    def put_out(self, player):
        if self.virtual == False:
            for sphere in self.focuscost:
                player.unusedFocus[sphere] -= self.focuscost[sphere]

    def is_blocked(self, player):
        Projectile.is_blocked(self, player)

    def activate(self, player, target_player, creature = None):
        if creature:
            player.deal_damage_to(self, target_player, self.damage, creature)
        else:
            player.deal_damage_to(self, target_player, self.damage)
        player.move_card_to(self, player.discard)
        player.unusedFocus[self.focustype] += self.focuscost[self.focustype]

class ColdWind(Projectile):

    cardname = 'Cold Wind'
    focustype = FROST
    focuscost = {FROST : 2}
    damage = 1
    text = 'Returns target creature to its player\'s hand, and deals 1 damage to that player.'

    def __init__(self):
        Projectile.__init__(self)

    def put_out(self, player):
        if self.virtual == False:
            for sphere in self.focuscost:
                player.unusedFocus[sphere] -= self.focuscost[sphere]

    def is_blocked(self, player):
        Projectile.is_blocked(self, player)

    def activate(self, player, target_player, creature = None):
        if creature:
            player.deal_damage_to(self, target_player, self.damage)
            creature.reset()
            target_player.move_card_to(creature, target_player.draw)
            target_player.draw.shuffle()
            print('{0}\'s {1} was blown back to their draw deck!'.format(target_player.name, creature.cardname))
        else:
            player.deal_damage_to(self, target_player, self.damage)
        player.move_card_to(self, player.discard)
        player.unusedFocus[FROST] += self.focuscost[FROST]

class Freeze(Projectile):

    cardname = 'Freeze'
    focustype = FROST
    focuscost = {FROST : 1}
    damage = 0
    count = 2
    text = 'Freezes a target creature for 2 turns.  Does not stack.  Does not affect Fire or Illusion.'

    def __init__(self):
        Projectile.__init__(self)

    def put_out(self, player):
        if self.virtual == False:
            for sphere in self.focuscost:
                player.unusedFocus[sphere] -= self.focuscost[sphere]

    def is_blocked(self, player):
        Projectile.is_blocked(self, player)

    def activate(self, player, target_player, creature = None):
        if creature:
            if creature.focustype not in (FIRE, ILLUSION):
                creature.take_condition(FROZEN, 2)
            else:
                print('{0} does not work on Fire or Illusion!  Did nothing!')
        else:
            print('{0} does nothing!'.format(self.cardname))
        player.move_card_to(self, player.discard)
        player.unusedFocus[FROST] += self.focuscost[FROST]               

class Voarthen(Creature):

    cardname = 'Voarthen'
    focustype = FROST
    focuscost = {FROST : 1}
    damage = 1
    health = 2
    text = 'Leap: When damaging a creature, deal 1 damage to its player as well.'

    def __init__(self):
        Creature.__init__(self)
        self.health = Voarthen.health

    def put_out(self, player):
        if self.virtual == False:
            for sphere in self.focuscost:
                player.unusedFocus[sphere] -= self.focuscost[sphere]

    def activate(self, player, target_player, creature = None):
        if creature:
            player.deal_damage_to(self, target_player, self.damage, creature)
            player.deal_damage_to(self, target_player, self.damage)
        else:
            player.deal_damage_to(self, target_player, self.damage)

    def reset(self):
        for x in self.conditions:
            self.conditions[x] = 0
        self.health = Voarthen.health
        self.damage = Voarthen.damage

    def die(self, player):
        self.reset()
        player.move_card_to(self, player.discard)
        player.unusedFocus[FROST] += self.focuscost[FROST]
        
        

    
