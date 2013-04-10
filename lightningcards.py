from card import *
from deck import *
from player import Player

class MetalWand(Focus):

    cardname = 'Metal Wand'
    focustype = LIGHTNING
    text = 'Provides 1 Lightning focus.'

    def __init__(self):
        Card.__init__(self)

    def put_out(self, player):
        player.focusTotal[LIGHTNING] += 1
        player.unusedFocus[LIGHTNING] += 1

    def when_remove_to_hand(self, player):
        player.focusTotal[LIGHTNING] -= 1
        player.unusedFocus[LIGHTNING] -= 1

    def when_remove_to_discard(self, player):
        player.focusTotal[LIGHTNING] -= 1
        player.unusedFocus[LIGHTNING] -= 1

    def when_remove_from_play(self, player):
        player.focusTotal[LIGHTNING] -= 1
        player.unusedFocus[LIGHTNING] -= 1

class Bolt(Projectile):

    cardname = 'Bolt'
    focustype = LIGHTNING
    focuscost = {LIGHTNING : 1}
    damage = 2
    text = 'Deal 2 damage to target Creature or player.  You may use an additional 1 focus to deal 1 further damage to the same target.'

    def __init__(self):
        Projectile.__init__(self)
        self.damage = Bolt.damage
        self.morefocus = 'n'

    def put_out(self, player):
        if player.unusedFocus[LIGHTNING] > 1:
            print('Do you want to spend 1 more Lightning focus to deal 1 additional damage? (y or n)')
            self.morefocus = input()
            if self.morefocus in ('yes','y'):
                self.damage += 1
                player.unusedFocus[LIGHTNING] -= 1
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
        if self.morefocus in ('yes','y'):
            player.unusedFocus[LIGHTNING] += 1
        if self.virtual == False:
            player.move_card_to(self, player.discard)
            player.unusedFocus[self.focustype] += self.focuscost[self.focustype]
            self.damage = Bolt.damage
        else:
            player.inPlay.remove(self)
        

class Flash(Augment):

    cardname = 'Flash'
    focustype = LIGHTNING
    focuscost = {LIGHTNING : 1}
    text = 'Play a copy of a Projectile in play for no extra focus cost.'

    def __init__(self):
        Card.__init__(self)

    def put_out(self, player, projectile):
        if self.virtual == False:
            for sphere in self.focuscost:
                player.unusedFocus[sphere] -= self.focuscost[sphere]
        copied = projectile.copy()
        print('Copied projectile!')
        player.inPlay.cards.append(copied)
        print('Projectile put in play!')
        copied.put_out(player)

    def activate(self, player):
        if self.virtual == False:
            player.move_card_to(self, player.discard)
            player.unusedFocus[self.focustype] += self.focuscost[self.focustype]
        else:
            player.inPlay.remove(self)
                
    

class BallLightning(Creature):

    cardname = 'Ball Lightning'
    focustype = LIGHTNING
    focuscost = {LIGHTNING : 2}
    damage = 2
    health = 1
    text = ''
    
    def __init__(self):
        Card.__init__(self)
        self.health = BallLightning.health

    def put_out(self, player):
        if self.virtual == False:
            for sphere in self.focuscost:
                player.unusedFocus[sphere] -= self.focuscost[sphere]

    def activate(self, player, target_player, creature = None):
        if creature:
            player.deal_damage_to(self, target_player, self.damage, creature)
        else:
            player.deal_damage_to(self, target_player, self.damage)

    def die(self, player):
        player.move_card_to(self, player.discard)
        player.unusedFocus[LIGHTNING] += self.focuscost[LIGHTNING]
    

    
        

    
