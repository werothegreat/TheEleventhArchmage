from card import *
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
        Card.__init__(self)
        self.damage = Bolt.damage

    def put_out(self, player):
        if player.unusedFocus[LIGHTNING] > 1:
            print('Do you want to spend 1 more Lightning focus to deal 1 additional damage? (y or n)')
            morefocus = input()
            if morefocus in ('yes','y'):
                self.damage += 1
                self.focuscost[LIGHTNING] += 1
        if self.virtual == False:
            for sphere in self.focuscost:
                player.unusedFocus[sphere] -= self.focuscost[sphere]
        

    def activate(self, player, target_player, creature = None):
        if creature:
            player.deal_damage_to(self, target_player, self.damage, creature)
        else:
            player.deal_damage_to(self, target_player, self.damage)
        player.move_card_to(self, player.discard)
        player.unusedFocus[self.focustype] += self.focuscost[self.focustype]

class Flash(Projectile):

    cardname = 'Flash'
    focustype = LIGHTNING
    focuscost = {LIGHTNING : 1}

    def __init__(self):
        Card.__init__(self)

    def put_out(self, player):
        if self.virtual == False:
            for sphere in self.focuscost:
                player.unusedFocus[sphere] -= self.focuscost[sphere]
        for x in player.inPlay.cards:
            if isinstance(x, Projectile) and not isinstance(x, Flash):
                hasotherproj = True
                break
            else:
                hasotherproj = False
        if hasotherproj == True:
            print('Projectiles in play:')
            for i in range(player.inPlay.cards[i]):
                if isinstance(player.inPlay.cards[i], Projectile) and not isinstance(player.inPlay.cards[i], Flash):
                    print('{0}){1} '.format(i,player.inPlay.cards[i]))
            print('Which projectile, aside from another Flash, do you want to play twice?  Enter its number.')
            while True:
                num = int(input())
                if num in range(player.inPlay.length()) and isinstance(player.inPlay.cards[i], Projectile) and not isinstance(player.inPlay.cards[i], Flash):
                    player.put_out_card(player.inPlay.cards[i].copy())
                    break
                else:
                    print('That\'s not a valid projectile.')
                
    

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
    

    
        

    
