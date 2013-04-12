from deck import Deck
from card import Card, Focus, FOCUS, Projectile, FROST
from frostcards import *
from lightningcards import *
from game import Game
from player import Player

myself = Player('Michael')
enemy = Player('Enemy', False)

thegame = Game(myself, enemy)

for i in range(7):
    myself.draw.add(MetalWand())
    myself.draw.add(Bolt())
for i in range(4):
    myself.draw.add(Flash())
    myself.draw.add(BallLightning())

for i in range(13):
    enemy.draw.add(FrostRing())
for i in range(7):
    enemy.draw.add(Icicle())
for i in range(2):
    enemy.draw.add(Voarthen())

'''for i in range(myself.draw.length()):
    print(myself.draw.cards[i].cardname)
    print(str(myself.draw.cards[i].id))

for i in range(enemy.draw.length()):
    print(enemy.draw.cards[i].cardname)
    print(str(enemy.draw.cards[i].id))'''

playagain = 'yes'
while playagain in ('yes','y'):

    thegame.start_game()

    turns = 1
    while enemy.health > 0 and myself.health > 0:
        thegame.begin_turn(myself)

        thegame.play_focus(myself)

        
        thegame.release_creature(myself)
            
                        
            
            

        if myself.hand.length() > 0:
            thegame.show_hand(myself)
            if (myself.have_inhand(Creature) or myself.have_inhand(Projectile)) and (myself.unusedFocus[LIGHTNING] >= myself.lowest_cost_inhand(LIGHTNING, Creature, Projectile)):
                print('Do you want to play a creature or projectile? (y or n)')
                playcard = input()
                while playcard in ('yes','y'):
                    print('Which card do you want to play?  Enter its number.')
                    handsize = myself.hand.length()
                    while handsize == myself.hand.length():
                        number = int(input())
                        if number in range(myself.hand.length()):
                            if not isinstance(myself.hand.cards[number], Projectile) and not isinstance(myself.hand.cards[number], Creature):
                                print('That is neither a creature nor a projectile.')
                            else:
                                myself.put_out_card(myself.hand.cards[number])
                        else:
                            print('That\'s not a valid card.')
                    print(' ')
                    if (myself.have_inhand(Creature) or myself.have_inhand(Projectile)) and myself.unusedFocus[LIGHTNING] > 0 and (myself.unusedFocus[LIGHTNING] >= myself.lowest_cost_inhand(LIGHTNING, Creature, Projectile)) and myself.hand.length() > 0:
                        print('You have {0} unused focus.'.format(str(myself.unusedFocus[LIGHTNING])))
                        print('Do you want to play another creature or projectile? (y or n)')
                        playcard = input()
                        if playcard in ('yes','y'):
                            thegame.show_hand(myself)
                    else:
                        playcard = 'n'
            if myself.have_inhand(Augment) and (myself.unusedFocus[LIGHTNING] >= myself.lowest_cost_inhand(LIGHTNING, Augment)) and myself.have_proj_inplay():
                thegame.show_hand(myself)
                print('Do you want to play an augment on a projectile? (y or n)')
                playcard = input()
                while playcard in ('yes','y'):
                    print('Which augment do you want to play?  Enter its number.')
                    while True:
                        aug = int(input())
                        if aug in range(myself.hand.length()):
                            if not isinstance(myself.hand.cards[aug], Augment):
                                print('That is not an augment.')
                            else:
                                print('You chose {0}.'.format(myself.hand.cards[aug].cardname))
                                break
                    print('{0}\'s projectiles:'.format(myself.name))
                    for i in range(myself.inPlay.length()):
                        if isinstance(myself.inPlay.cards[i], Projectile):
                            print(str(i)+') '+myself.inPlay.cards[i].cardname+', ', end = '')
                    print(' ')
                    print('Which projectile do you want to augment? Enter its number.')
                    while True:
                        proj = int(input())
                        if proj in range(myself.inPlay.length()):
                            if not isinstance(myself.inPlay.cards[proj], Projectile):
                                print('That is not a projectile')
                            else:
                                print('You chose to augment {0} with {1}.'.format(myself.inPlay.cards[proj].cardname, myself.hand.cards[aug].cardname))
                                myself.put_out_card(myself.hand.cards[aug], myself.inPlay.cards[proj])
                                break
                    if myself.have_inhand(Augment) and (myself.unusedFocus[LIGHTNING] >= myself.lowest_cost_inhand(LIGHTNING, Augment)) and myself.have_proj_inplay():
                        thegame.show_hand(myself)
                        print('Do you want to play another augment on a projectile? (y or n)')
                        playcard = input()
                    else:
                        playcard = 'n'
                

        thegame.show_inplay(myself)
        for x in range(myself.inPlay.length()):
            if isinstance(myself.inPlay.cards[x], Projectile):
                has_proj = True
                break
            else:
                has_proj = False
        while has_proj == True:
            for x in range(myself.inPlay.length()):
                if isinstance(myself.inPlay.cards[x], Projectile):
                    if enemy.have_creature_inplay():
                        print('{0} has creatures in play.  Do you want to target one with {1}? (y or n)'.format(enemy.name, myself.inPlay.cards[x].cardname))
                        hitcreature = input()
                        if hitcreature in ('yes','y'):
                            print('{0}\'s creatures:'.format(enemy.name))
                            for i in range(enemy.inPlay.length()):
                                if isinstance(enemy.inPlay.cards[i], Creature):
                                    print(str(i)+') '+enemy.inPlay.cards[i].cardname+', ', end = '')
                            print(' ')
                            print('Which creature do you want to target?  Enter its number.')
                            while True:
                                number = int(input())
                                if number in range(enemy.inPlay.length()) and isinstance(enemy.inPlay.cards[number], Creature):
                                    myself.activate_card(myself.inPlay.cards[x], enemy, enemy.inPlay.cards[number])
                                    break
                                else:
                                    print('That\'s not a valid card.')
                            break
                        else:
                            myself.activate_card(myself.inPlay.cards[x], enemy)
                            break
                    else:
                        myself.activate_card(myself.inPlay.cards[x], enemy)
                        break
            for x in range(myself.inPlay.length()):
                if isinstance(myself.inPlay.cards[x], Projectile):
                    has_proj = True
                    break
                else:
                    has_proj = False
        for x in range(myself.inPlay.length()):
            if isinstance(myself.inPlay.cards[x], Creature):
                if enemy.have_creature_inplay():
                    print('{0} has creatures in play.  Do you want to target one with {1}? (y or n)'.format(enemy.name, myself.inPlay.cards[x].cardname))
                    hitcreature = input()
                    if hitcreature in ('yes','y'):
                        print('{0}\'s creatures:'.format(enemy.name))
                        for i in range(enemy.inPlay.length()):
                            if isinstance(enemy.inPlay.cards[i], Creature):
                                print(str(i)+') '+enemy.inPlay.cards[i].cardname+', ', end = '')
                        print(' ')
                        print('Which creature do you want to target?  Enter its number.')
                        playsize = enemy.inPlay.length()
                        while True:
                            number = int(input())
                            if number in range(enemy.inPlay.length()) and isinstance(enemy.inPlay.cards[number], Creature):
                                myself.activate_card(myself.inPlay.cards[x], enemy, enemy.inPlay.cards[number])
                                break
                            else:
                                print('That\'s not a valid card.')
                    else:
                        myself.activate_card(myself.inPlay.cards[x], enemy)
                else:
                    myself.activate_card(myself.inPlay.cards[x], enemy)
                    
        for x in range(myself.inPlay.length()):
            if isinstance(myself.inPlay.cards[x], Augment):
                has_aug = True
                break
            else:
                has_aug = False
        while has_aug == True:
            for x in range(myself.inPlay.length()):
                if isinstance(myself.inPlay.cards[x], Augment):
                    myself.activate_card(myself.inPlay.cards[x])
                    break
            for x in range(myself.inPlay.length()):
                if isinstance(myself.inPlay.cards[x], Augment):
                    has_aug = True
                    break
                else:
                    has_aug = False
                    
        print('Enemy is at '+str(enemy.health)+' health.')

        if enemy.health <= 0:
            print('Your enemy is dead!  You win!')
            break

        if myself.draw.length() == 0:
            print('Your deck is empty!  You lose!')
            break

        myself.draw_card()

        thegame.begin_turn(enemy)
        thegame.show_hand(enemy)
        '''if enemy.have_inhand(Focus):
            for x in range(enemy.hand.length()):
                if enemy.hand.cards[x].cardtype == FOCUS:
                    print('Enemy has played {}!'.format(enemy.hand.cards[x].cardname))
                    enemy.put_out_card(enemy.hand.cards[x])
                    break
        print('Enemy has {} unused focus.'.format(enemy.unusedFocus[FROST]))'''

        thegame.play_focus(enemy)

        while (enemy.have_inhand(Creature) or enemy.have_inhand(Projectile)) and (enemy.unusedFocus[FROST] >= enemy.lowest_cost_inhand(FROST, Creature, Projectile)) and enemy.hand.length() > 0:
            for x in range(enemy.hand.length()):
                if enemy.hand.cards[x].cardtype != FOCUS and enemy.hand.cards[x].focuscost[FROST] <= enemy.unusedFocus[FROST]:
                    enemy.put_out_card(enemy.hand.cards[x])
                    break
                
        
        print('Cards in play:')
        for x in range(enemy.inPlay.length()):
            if not isinstance(enemy.inPlay.cards[x], Focus):
                print(str(x)+') '+enemy.inPlay.cards[x].cardname+', ', end = '')
        print(' ')
        for x in range(enemy.inPlay.length()):
            if isinstance(enemy.inPlay.cards[x], Projectile):
                has_proj = True
                break
            else:
                has_proj = False
        while has_proj == True:
            for x in range(enemy.inPlay.length()):
                if isinstance(enemy.inPlay.cards[x], Projectile):
                    enemy.activate_card(enemy.inPlay.cards[x], myself)
                    break
            for x in range(enemy.inPlay.length()):
                if isinstance(enemy.inPlay.cards[x], Projectile):
                    has_proj = True
                    break
                else:
                    has_proj = False
        for x in range(enemy.inPlay.length()):
            if isinstance(enemy.inPlay.cards[x], Creature):
                enemy.activate_card(enemy.inPlay.cards[x], myself)
            
        print('{0} is at {1} health.'.format(myself.name, str(myself.health)))

        if myself.health <= 0:
            print('You died!  You lose!')
            break

        if enemy.draw.length() == 0:
            print('Enemy\'s deck is empty!  You win!')
            break
            

        enemy.draw_card()
        print(' ')
        turns += 1
    
        

    thegame.end_game()
    print('Do you want to play again?')
    playagain = input()
        
