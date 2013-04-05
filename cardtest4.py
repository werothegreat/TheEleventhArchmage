from deck import Deck
from card import Card, Focus, Projectile, FROST
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

    while enemy.health > 0:
        print('Cards in hand:')
        for x in range(myself.hand.length()):
            print(str(x)+') '+myself.hand.cards[x].cardname+', ', end = '')
        print(' ')

        print('Which card do you want to play?  Enter its number.')
        handsize = myself.hand.length()
        while handsize == myself.hand.length():
            number = int(input())
            if number in range(myself.hand.length()):
                myself.put_out_card(myself.hand.cards[number])
                print('Played {0}.'.format(myself.hand.cards[number].cardname))
            else:
                print('That\'s not a valid card.')
        print('Enemy is at '+str(enemy.health)+' health.')
        print('You have {0} unused focus.'.format(str(myself.focusTotal[FROST] - myself.usedFocus[FROST])))
        #myself.draw_card()
        #PROBLEMS
    
        

    print('My draw is {0}'.format(myself.draw.length()))
    print('My hand is {0}'.format(myself.hand.length()))
    myself.hand.shuffle_into(myself.draw)
    print('Shuffled!')
    print('My draw is {0}'.format(myself.draw.length()))
    print('My hand is {0}'.format(myself.hand.length()))
    myself.inPlay.shuffle_into(myself.draw)
    myself.discard.shuffle_into(myself.draw)
    print('Do you want to play again?')
    playagain = input()
        
