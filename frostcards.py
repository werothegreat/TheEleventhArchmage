from card import Card, FOCUS, PROJECTILE, EFFECT, CREATURE, FROST
from player import Player

class FrostRing(Card):

    cardtype = FOCUS
    cardname = 'Frost Ring'
    

    def __init__(self):
        Card.__init__(self)

    def put_out(self, game, player):
        if FROST not in player.focusTotal:
            player.focusTotal[FROST] = 1
        else:
            player.focusTotal[FROST] += 1

    def when_remove_to_hand(self, game, player):
        player.focusTotal[FROST] -= 1

    def when_remove_to_discard(self, game, player):
        player.focusTotal[FROST] -= 1

class Icicle(Card):

    cardtype = PROJECTILE
    cardname = 'Icicle'
    focuscost = {FROST : 1}

    def __init__(self):
        Card.__init__(self)

    def activate(self, game, player, target_player):
        player.deal_damage_to(self, target_player, 2)
        

    
