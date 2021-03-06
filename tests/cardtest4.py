from deck import Deck
from card import Card, Focus, FOCUS, Projectile, FROST
from frostcards import * 
from player import Player

myself = Player('Michael','boob')
enemy = Player('Enemy','boob')

for i in range(7):
    myself.draw.add(FrostRing())
    myself.draw.add(Icicle())
for i in range(4):
    myself.draw.add(ColdWind())
    myself.draw.add(Voarthen())

for i in range(13):
    enemy.draw.add(FrostRing())
for i in range(7):
    enemy.draw.add(Icicle())
for i in range(2):
    enemy.draw.add(Voarthen())

myself.draw.shuffle()
enemy.draw.shuffle()

'''for i in range(myself.draw.length()):
    print(myself.draw.cards[i].cardname)
    print(str(myself.draw.cards[i].id))

for i in range(enemy.draw.length()):
    print(enemy.draw.cards[i].cardname)
    print(str(enemy.draw.cards[i].id))'''

playagain = 'yes'
while playagain in ('yes','y'):

    myself.draw_card(7)
    print('Drew cards!')
    enemy.draw_card(7)
    print('Enemy draw cards!')

    turns = 1
    while enemy.health > 0 and myself.health > 0:
        print('Turn {}:'.format(str(turns)))
        print('You have {0} unused focus.'.format(str(myself.unusedFocus[FROST])))
        print('Cards in hand:')
        for x in range(myself.hand.length()):
            print(str(x)+') '+myself.hand.cards[x].cardname+', ', end = '')
        print(' ')


        while myself.have_focus_inhand() == False and turns == 1:
            print('You mulligan.')
            myself.hand.shuffle_into(myself.draw)
            myself.draw_card(7)
            print('Cards in hand:')
            for x in range(myself.hand.length()):
                print(str(x)+') '+myself.hand.cards[x].cardname+', ', end = '')
            print(' ')

        while enemy.have_focus_inhand() == False and turns == 1:
            print('Enemy mulligans.')
            enemy.hand.shuffle_into(enemy.draw)
            enemy.draw_card(7)

        if myself.have_focus_inhand() == True:
            print('You may play a focus from your hand.  Enter its number.')
            print(' ')
            handsize = myself.hand.length()
            while handsize == myself.hand.length():
                chosen_focus_number = int(input())
                if chosen_focus_number in range(myself.hand.length()) and myself.hand.cards[chosen_focus_number].cardtype == FOCUS:
                    myself.put_out_card(myself.hand.cards[chosen_focus_number])
                elif chosen_focus_number in range(myself.hand.length()) and myself.hand.cards[chosen_focus_number].cardtype != FOCUS:
                    print('That\'s not a focus.')
                else:
                    print('That\'s not a valid card.')
            print('You have {0} unused focus.'.format(str(myself.unusedFocus[FROST])))
            print('Cards in hand:')
            for x in range(myself.hand.length()):
                print(str(x)+') '+myself.hand.cards[x].cardname+', ', end = '')
            print(' ')

        if myself.have_creature_inplay() == True:
            print('Creatures in play:')
            for x in range(myself.inPlay.length()):
                if isinstance(myself.inPlay.cards[x], Creature):
                    print(str(x)+') '+myself.inPlay.cards[x].cardname+', ', end = '')
            print(' ')
            print('Do you want to release a creature? (y or n)')
            release = input()
            while release in ('yes','y'):
                print('Which creature do you want to release?  Enter its number.')
                playsize = myself.inPlay.length()
                while playsize == myself.inPlay.length():
                    number = int(input())
                    if number in range(myself.inPlay.length()) and isinstance(myself.inPlay.cards[number], Creature):
                        print('{0} has been released.'.format(myself.inPlay.cards[number].cardname))
                        myself.inPlay.cards[number].die(myself)
                    else:
                        print('That\'s not a valid creature.')
                print(' ')
                print('You have {0} unused focus.'.format(str(myself.unusedFocus[FROST])))
                if myself.have_creature_inplay() == True:
                    print('Do you want to release another creature? (y or n)')
                    release = input()
                else:
                    release = 'n'
            
                        
            
            

        if myself.hand.length() > 0:
                    
            if myself.have_nonfocus_inhand() == True and (myself.unusedFocus[FROST] >= myself.lowest_cost_inhand(FROST)):
                print('Do you want to play a card? (y or n)')
                playcard = input()
                while playcard in ('yes','y'):
                    print('Which card do you want to play?  Enter its number.')
                    handsize = myself.hand.length()
                    while handsize == myself.hand.length():
                        number = int(input())
                        if number in range(myself.hand.length()):
                            if myself.hand.cards[number].cardtype == FOCUS:
                                print('You may only play one focus per turn.')
                            else:
                                myself.put_out_card(myself.hand.cards[number])
                        else:
                            print('That\'s not a valid card.')
                    print(' ')
                    if myself.have_nonfocus_inhand() == True and myself.unusedFocus[FROST] > 0 and (myself.unusedFocus[FROST] >= myself.lowest_cost_inhand(FROST)) and myself.hand.length() > 0:
                        print('You have {0} unused focus.'.format(str(myself.unusedFocus[FROST])))
                        print('Do you want to play another card? (y or n)')
                        playcard = input()
                        if playcard in ('yes','y'):
                            print('Cards in hand:')
                            for x in range(myself.hand.length()):
                                print(str(x)+') '+myself.hand.cards[x].cardname+', ', end = '')
                            print(' ')
                    else:
                        playcard = 'n'
                

        print('Cards in play:')
        for x in range(myself.inPlay.length()):
            if myself.inPlay.cards[x].cardtype != FOCUS:
                print(str(x)+') '+myself.inPlay.cards[x].cardname+', ', end = '')
        print(' ')
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
                            playsize = enemy.inPlay.length()
                            while playsize == enemy.inPlay.length():
                                number = int(input())
                                if number in range(enemy.inPlay.length()) and isinstance(enemy.inPlay.cards[number], Creature):
                                    myself.activate_card(myself.inPlay.cards[x], enemy, enemy.inPlay.cards[number])
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
                        while playsize == enemy.inPlay.length():
                            number = int(input())
                            if number in range(enemy.inPlay.length()) and isinstance(enemy.inPlay.cards[number], Creature):
                                myself.activate_card(myself.inPlay.cards[x], enemy, enemy.inPlay.cards[number])
                            else:
                                print('That\'s not a valid card.')
                    else:
                        myself.activate_card(myself.inPlay.cards[x], enemy)
                else:
                    myself.activate_card(myself.inPlay.cards[x], enemy)
        print('Enemy is at '+str(enemy.health)+' health.')

        if enemy.health <= 0:
            print('Your enemy is dead!  You win!')
            break

        if myself.draw.length() == 0:
            print('Your deck is empty!  You lose!')
            break

        myself.draw_card()

        print('Now Enemy goes.')
        print('Cards in hand:')
        for x in range(enemy.hand.length()):
            print(str(x)+') '+enemy.hand.cards[x].cardname+', ', end = '')
        print(' ')
        if enemy.have_focus_inhand() == True:
            for x in range(enemy.hand.length()):
                if enemy.hand.cards[x].cardtype == FOCUS:
                    print('Enemy has played {}!'.format(enemy.hand.cards[x].cardname))
                    enemy.put_out_card(enemy.hand.cards[x])
                    break
        print('Enemy has {} unused focus.'.format(enemy.unusedFocus[FROST]))

        while enemy.have_nonfocus_inhand() == True and (enemy.unusedFocus[FROST] >= enemy.lowest_cost_inhand(FROST)) and enemy.hand.length() > 0:
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
    
        

    myself.end_game_cleanup()
    enemy.end_game_cleanup()
    print('Do you want to play again?')
    playagain = input()
        
