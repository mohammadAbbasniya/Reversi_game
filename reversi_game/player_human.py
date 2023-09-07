from reversi_game import Player
from reversi_game import Reversi


class HumanPlayer(Player):

    def get_move(self, reversi: 'Reversi', possible_moves: 'list', pid: 'int'):
        while True:
            inp = input('enter (row  column): ')
            inps = inp.split(' ')
            if len(inps) == 2:
                x, y = inps
                if x.isnumeric() and y.isnumeric():
                    x, y = int(x), int(y)
                    if (x, y) in possible_moves:
                        return x, y
                    else:
                        print('invalid input, your choice is not a possible move')
                else:
                    print('invalid input, you must enter integers')
            else:
                print('invalid input, just enter two numbers (row column) seperated by a single space')
