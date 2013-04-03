from card import FOCUS, PROJECTILE, EFFECT, CREATURE, FROST

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
        
