import random, time

#publish, damn you, github!

deck = []
hand = []
inPlay = []
discard = []
enemyHealth = 25

def shuffle(cards):
    random.shuffle(cards)

def drawCard(carddeck):
    top = len(carddeck)
    hand.append(carddeck[top-1])
    del carddeck[top-1]

def playCard(card):
    inPlay.append(hand[card])
    del hand[card]

def discardFromPlay(card):
    discard.append(inPlay[card])
    del inPlay[card]

for x in range(7):
    deck.append('icicle')

for x in range(7):
    deck.append('butt')

playagain = 'yes'
while playagain in ('yes','y'):
    myDeck = []
    myDeck = deck
    shuffle(myDeck)

    for x in range(7):
        drawCard(myDeck)

    health = enemyHealth
    while health > 0:
        print('Cards in hand:')
        for x in range(len(hand)):
            print(str(x) + ') ' + str(hand[x]))
        print(' ')

        print('Pick the number of the card you want to play.')
        handsize = len(hand)
        while handsize == len(hand):
            number = 0
            number = int(input())
            if number in range(handsize):
                if str(hand[number]) == 'icicle':
                    health -= 5
                playCard(number)
                for x in range(len(inPlay)):
                    print(inPlay[x])
            else:
                print('That\'s not a valid card.')

        
        

        drawCard(myDeck)

    print('You beat the monster!')
    print('Do you want to play again?')
    playagain = input()
