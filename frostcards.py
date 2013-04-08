from card import * #Card, Focus, Projectile, EFFECT, CREATURE, FROST
from player import Player

class FrostRing(Focus):

    cardname = 'Frost Ring'
    focustype = FROST
    

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

    def __init__(self):
        Card.__init__(self)

    def activate(self, player, target_player, creature = None):
        if creature:
            player.deal_damage_to(self, target_player, self.damage, creature)
        else:
            player.deal_damage_to(self, target_player, self.damage)
        player.move_card_to(self, player.discard)
        player.unusedFocus[FROST] += self.focuscost[FROST]

class ColdWind(Projectile):

    cardname = 'Cold Wind'
    focustype = FROST
    focuscost = {FROST : 2}
    damage = 1

    def __init__(self):
        Card.__init__(self)

    def activate(self, player, target_player, creature = None):
        if creature:
            player.deal_damage_to(self, target_player, self.damage)
            target_player.move_card_to(creature, target_player.hand)
            print('{0}\'s {1} was blown back to their hand!'.format(target_player.name, creature.cardname))
        else:
            player.deal_damage_to(self, target_player, self.damage)
            player.move_card_to(self, player.discard)
            player.unusedFocus[FROST] += self.focuscost[FROST]

class Voarthen(Creature):

    cardname = 'Voarthen'
    focustype = FROST
    focuscost = {FROST : 1}
    damage = 1
    health = 2

    def __init__(self):
        Card.__init__(self)
        self.health = Voarthen.health

    def activate(self, player, target_player, creature = None):
        if creature:
            player.deal_damage_to(self, target_player, self.damage, creature)
        else:
            player.deal_damage_to(self, target_player, self.damage)

    def die(self, player):
        player.move_card_to(self, player.discard)
        player.unusedFocus[FROST] += self.focuscost[FROST]
        
        

    
