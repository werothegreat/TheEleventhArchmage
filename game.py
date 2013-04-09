from player import *

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
            
    def end_game(self):
        #Resets turns and cleans up players
        for x in self.players:
            self.turn[x.name] = 0
            x.end_game_cleanup()
    
        
