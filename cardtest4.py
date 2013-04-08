from deck import Deck
from card import Card, Focus, FOCUS, Projectile, FROST
from frostcards import * #FrostRing, Icicle, ColdWind
from player import Player

myself = Player('Michael','boob')
enemy = Player('Enemy','boob')

for i in range(7):
    myself.draw.add(FrostRing())
    myself.draw.add(Icicle())
for i in range(6):
    myself.draw.add(ColdWind())

for i in range(13):
    enemy.draw.add(FrostRing())
for i in range(7):
    enemy.draw.add(Icicle())

myself.draw.shuffle()
enemy.draw.shuffle()

for i in range(myself.draw.length()):
    print(myself.draw.cards[i].cardname)
    print(str(myself.draw.cards[i].id))

for i in range(enemy.draw.length()):
    print(enemy.draw.cards[i].cardname)
    print(str(enemy.draw.cards[i].id))

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
            if myself.inPlay.cards[x].cardtype != FOCUS:
                has_attack = True
                break
            else:
                has_attack = False
        while has_attack == True:
            for x in range(myself.inPlay.length()):
                if myself.inPlay.cards[x].cardtype != FOCUS:
                    myself.activate_card(myself.inPlay.cards[x], enemy)
                    break
            for x in range(myself.inPlay.length()):
                if myself.inPlay.cards[x].cardtype != FOCUS:
                    has_attack = True
                    break
                else:
                    has_attack = False
        print('Enemy is at '+str(enemy.health)+' health.')

        if enemy.health <= 0:
            print('Your enemy is dead!  You win!')
            break

        print('Now Enemy goes.')
        if enemy.have_focus_inhand() == True:
            for x in range(enemy.hand.length()):
                if enemy.hand.cards[x].cardtype == FOCUS:
                    print('Enemy has played {}!'.format(enemy.hand.cards[x].cardname))
                    enemy.put_out_card(enemy.hand.cards[x])
                    break
        print('Enemy has {} unused focus.'.format(enemy.unusedFocus[FROST]))
            
            
        
        
        elif len(myself.draw.cards) == 0:
            print('Your deck is empty!  You lose!')
            break
        myself.draw_card()
        print(' ')
        turns += 1
    
        

    '''print('My draw is {0}'.format(myself.draw.length()))
    print('My hand is {0}'.format(myself.hand.length()))'''
    myself.hand.shuffle_into(myself.draw)
    print('Shuffled!')
    '''print('My draw is {0}'.format(myself.draw.length()))
    print('My hand is {0}'.format(myself.hand.length()))'''
    myself.inPlay.shuffle_into(myself.draw)
    myself.discard.shuffle_into(myself.draw)
    print('Do you want to play again?')
    playagain = input()
        
