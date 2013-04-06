from deck import Deck
from card import Card, Focus, FOCUS, Projectile, FROST
from frostcards import FrostRing, Icicle
from player import Player

myself = Player('Michael','boob')
enemy = Player('Enemy','boob')

for i in range(7):
    myself.draw.add(FrostRing())
    myself.draw.add(Icicle())

myself.draw.shuffle()

for i in range(myself.draw.length()):
    print(myself.draw.cards[i].cardname)
    print(str(myself.draw.cards[i].id))

playagain = 'yes'
while playagain in ('yes','y'):

    for x in range(7):
        myself.draw_card()
        print('Drew a card!')

    turns = 1
    while enemy.health > 0:
        print('Turn {}:'.format(str(turns)))
        print('You have {0} unused focus.'.format(str(myself.unusedFocus[FROST])))
        print('Cards in hand:')
        for x in range(myself.hand.length()):
            print(str(x)+') '+myself.hand.cards[x].cardname+', ', end = '')
        print(' ')

        for x in range(myself.hand.length()):
            if myself.hand.cards[x].cardtype == FOCUS:
                have_focus = True
                print('You may play a focus from your hand.  Enter its number.')
                print(' ')
                break
            else:
                have_focus = False

        if have_focus == False and turns == 1:
            print('You mulligan.')
            break

        if have_focus == True:
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
            for x in range(myself.hand.length()):
                if myself.hand.cards[x].cardtype != FOCUS:
                    have_nonfocus = True
                    break
                else:
                    have_nonfocus = False
            highest_cost = 0
            for x in range(myself.hand.length()):
                if myself.hand.cards[x].cardtype != FOCUS and myself.hand.cards[x].focuscost[FROST] > highest_cost:
                    highest_cost = myself.hand.cards[x].focuscost[FROST]
                    
            if have_nonfocus == True and (myself.unusedFocus[FROST] >= highest_cost):
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
                    for x in range(myself.hand.length()):
                        if myself.hand.cards[x].cardtype != FOCUS:
                            have_nonfocus = True
                            break
                        else:
                            have_nonfocus = False
                    for x in range(myself.hand.length()):
                        if myself.hand.cards[x].cardtype != FOCUS and myself.hand.cards[x].focuscost[FROST] > highest_cost:
                            highest_cost = myself.hand.cards[x].focuscost[FROST]
                    if have_nonfocus == True and (myself.unusedFocus[FROST] >= highest_cost) and myself.hand.length() > 0:
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
        if len(myself.draw.cards) == 0:
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
        
