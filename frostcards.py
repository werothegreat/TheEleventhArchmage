from card import Card, FOCUS, PROJECTILE, EFFECT, CREATURE

class FrostRing(Card):

    cardtype = FOCUS
    focuscost = 0
    focustype = 'Frost'

    def put_out(self):
        
