from card import Card, Focus, Projectile, EFFECT, CREATURE, FROST
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

class Icicle(Projectile):

    cardname = 'Icicle'
    focustype = FROST
    focuscost = {FROST : 1}

    def __init__(self):
        Card.__init__(self)

    

    def activate(self, player, target_player):
        player.deal_damage_to(self, target_player, 2)
        

    
