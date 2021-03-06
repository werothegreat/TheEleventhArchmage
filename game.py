from player import *
from card import *

class Game(object):
    
    def __init__(self, *player):
        #creates a game
        self.players = player
        self.active_player = None
        self.turn = {}
        for x in self.players:
            self.turn[x.name] = 0

    def start_game(self):
        #Draws your starting hand and checks for mulligans
        for x in self.players:
            x.draw.shuffle()
            x.draw_card(7)
            count = 1
            while x.have_inhand(Focus) == False and count < 5:
                print('{0} mulligans.'.format(x.name))
                x.hand.shuffle_into(x.draw)
                x.draw_card(7)
                count += 1
            if count == 5:
                print('{0} obviously has no focuses in their deck, and is going to lose.'.format(x.name))

    def begin_turn(self, player):
        self.turn[player.name] += 1
        print('{0} turn {1}:'.format(player.name, self.turn[player.name]))
        if player.has_unused_focus():
            print('Unused focus:')
            for sphere in player.unusedFocus:
                if player.unusedFocus[sphere] > 0:
                    print('{0}: {1} '.format(sphere, player.unusedFocus[sphere]), end = '')
            print(' ')
        else:
            print('{0} has no unused focus.'.format(player.name))

    def show_hand(self, player):
        print('Cards in {0}\'s hand:'.format(player.name))
        for x in range(player.hand.length()):
            print('{0}){1} '.format(str(x),player.hand.cards[x].cardname), end = '')
        print(' ')

    def show_inplay(self, player):
        print('Cards {0} has in play:'.format(player.name))
        for x in range(player.inPlay.length()):
            if not isinstance(player.inPlay.cards[x], Focus):
                print('{0}){1} '.format(str(x),player.inPlay.cards[x].cardname), end = '')
        print(' ')

    def play_focus(self, player):
        if player.have_inhand(Focus):
            print('{0} may play a focus from their hand.'.format(player.name))
            if player.is_human():
                self.show_hand(player)
                print('Enter its number:')
                while True:
                    cfn = int(input())#chosen focus number
                    if cfn in range(player.hand.length()) and isinstance(player.hand.cards[cfn], Focus):
                        print('{0} has played {1}, adding 1 to their {2} focus.'.format(player.name, player.hand.cards[cfn].cardname, player.hand.cards[cfn].focustype))
                        player.put_out_card(player.hand.cards[cfn])
                        break
                    else:
                        print('That\'s not a valid choice.')
            else:
                if player.have_inhand(Focus):
                    for x in range(player.hand.length()):
                        if isinstance(player.hand.cards[x], Focus):
                            print('{0} has played {1}, adding 1 to their {2} focus.'.format(player.name, player.hand.cards[x].cardname, player.hand.cards[x].focustype))
                            player.put_out_card(player.hand.cards[x])
                            break
        

    def release_creature(self, player):
        if player.is_human():
            if player.have_inplay(Creature):
                self.show_inplay(player)
                print('Do you want to release a creature? (y or n)')
                release = input()
                while release in ('yes','y'):
                    print('Which creature do you want to release?  Enter its number.')
                    while True:
                        ccn = int(input())#chosen creature number
                        if ccn in range(player.inPlay.length()) and isinstance(player.inPlay.cards[ccn], Creature):
                            print('{0} has been released.'.format(player.inPlay.cards[ccn].cardname))
                            player.inPlay.cards[ccn].die(player)
                            break
                        else:
                            print('That\'s not a valid creature.')
                    print(' ')
                    print('Unused focus:')
                    for sphere in player.unusedFocus:
                        if player.unusedFocus[sphere] > 0:
                            print('{0}: {1} '.format(sphere, player.unusedFocus[sphere]), end = '')
                    print(' ')
                    if player.have_inplay(Creature):
                        print('Do you want to release another creature? (y or n)')
                        release = input()
                    else:
                        release = 'n'

    def play_creatureproj(self, player):
        if (player.have_inhand(Creature) or player.have_inhand(Projectile)) and player.able_to_play_type(Creature, Projectile):
            if player.is_human():
                self.show_hand(player)
                print('Do you want to play a creature or projectile? (y or n)')
                playcard = input()
                while playcard in ('yes','y'):
                    print('Which card do you want to play?  Enter its number.')
                    while True:
                        ccpn = int(input())#chosen creature-projectile number
                        if ccpn in range(player.hand.length()) and (isinstance(player.hand.cards[ccpn], Creature) or isinstance(player.hand.cards[ccpn], Projectile)) and player.able_to_play_card(player.hand.cards[ccpn]):
                            print('{0} has played {1}.'.format(player.name, player.hand.cards[ccpn].cardname))
                            player.put_out_card(player.hand.cards[ccpn])
                            break
                        else:
                            print('That\'s not a valid selection.')
                    print(' ')
                    if (player.have_inhand(Creature) or player.have_inhand(Projectile)) and player.able_to_play_type(Creature, Projectile):
                        print('Unused focus:')
                        for sphere in player.unusedFocus:
                            if player.unusedFocus[sphere] > 0:
                                print('{0}: {1} '.format(sphere, player.unusedFocus[sphere]), end = '')
                        print(' ')
                        print('Do you want to play another creature or projectile? (y or n)')
                        playcard = input()
                        if playcard in ('yes','y'):
                            self.show_hand(player)
                    else:
                        playcard = 'n'
            else:
                while (player.have_inhand(Creature) or player.have_inhand(Projectile)) and player.able_to_play_type(Creature, Projectile):
                    for x in range(player.hand.length()):
                        if (isinstance(player.hand.cards[x], Creature) or isinstance(player.hand.cards[x], Projectile)) and player.able_to_play_card(player.hand.cards[x]):
                            player.put_out_card(player.hand.cards[x])
                            break

    def play_augment(self, player):
        if player.have_inhand(Augment) and player.able_to_play_type(Augment) and player.have_inplay(Projectile):
            if player.is_human():
                self.show_hand(player)
                print('Do you want to play an augment on a projectile? (y or n)')
                playaug = input()
                while playaug in ('yes','y'):
                    print('Which augment do you want to play?  Enter its number.')
                    while True:
                        can = int(input())#chosen augment number
                        if can in range(player.hand.length()) and isinstance(player.hand.cards[can], Augment) and player.able_to_play_card(player.hand.cards[can]):
                            print('You chose {0}.'.format(player.hand.cards[can].cardname))
                            break
                        else:
                            print('That\'s not a valid selection.')
                    self.show_inplay(player)
                    print('Which projectile do you want to augment?  Enter its number.')
                    while True:
                        cpn = int(input())#chosen projectile number
                        if cpn in range(player.inPlay.length()) and isinstance(player.inPlay.cards[cpn], Projectile):
                            print('{0} has played {1}, augmenting {2}.'.format(player.name, player.hand.cards[can].cardname, player.inPlay.cards[cpn].cardname))
                            player.put_out_card(player.hand.cards[can], player.inPlay.cards[cpn])
                            break
                        else:
                            print('That\'s not a valid selection.')
                    print(' ')
                    if player.have_inhand(Augment) and player.able_to_play_type(Augment) and player.have_inplay(Projectile):
                        print('Unused focus:')
                        for sphere in player.unusedFocus:
                            if player.unusedFocus[sphere] > 0:
                                print('{0}: {1} '.format(sphere, player.unusedFocus[sphere]), end = '')
                        print(' ')
                        print('Do you want to play another augment? (y or n)')
                        playaug = input()
                        if playaug in ('yes','y'):
                            self.show_hand(player)
                    else:
                        playaug = 'n'
                

    def activate_cards(self, player):
        pass

    def end_of_turn(self, player):
        for x in self.players:
            print('{0} is at {1} health, and has {2} cards in their draw deck.'.format(player.name, player.health, str(player.hand.length())))
        player.draw_card()
        

    def player_turn(self, player):
        #Eventually, will encompass all the above methods
        #to produce one player's whole turn
        pass
            
    def end_game(self):
        #Resets turns and cleans up players
        for x in self.players:
            self.turn[x.name] = 0
            x.end_game_cleanup()
    
        
