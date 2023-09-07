from reversi_game import ReversiConsoleUI
from reversi_game import HumanPlayer
from reversi_game import AIPlayer
import os


def get_human_color():
    print('Please choose color for Human player:')
    print('  1) White o')
    print('  2) Black ●')
    while True:
        choice = input('>>> ')
        if choice == '1':
            return 1
        elif choice == '2':
            return 2
        else:
            print('Invalid input, just enter 1 or 2.')


def get_players():
    print('Please choose game mode:')
    print('  1) Play Human vs Human')
    print('  2) Play Human vs AI')
    while True:
        choice = input('>>> ')
        if choice == '1':
            return HumanPlayer('o'), HumanPlayer('●')
        elif choice == '2':
            if get_human_color() == 1:
                return HumanPlayer('o'), AIPlayer('●')
            else:
                return HumanPlayer('●'), AIPlayer('o')
        else:
            print('Invalid input, just enter 1 or 2.')


if __name__ == '__main__':
    os.system("color f0")

    player1, player2 = get_players()
    reversi = ReversiConsoleUI(8, player1, player2)
    reversi.run()
