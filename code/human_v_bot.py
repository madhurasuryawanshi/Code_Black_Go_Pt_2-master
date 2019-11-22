from __future__ import print_function
# tag::play_against_your_bot[]
from code.dlgo import agent
from code.dlgo import goboard_slow as goboard, gotypes
from code.dlgo.utils import print_board, print_move, point_from_coords
from six.moves import input


def main():
    board_size = 0
    while not 5 <= board_size <= 19:
        board_size = int(input("Enter Board Size (5X5 - 19X19) : "))
    game = goboard.GameState.new_game(board_size)
    bot = agent.RandomBot()

    while not game.is_over():
        #print(chr(27) + "[2J")
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            if human_move == 'pass':
                move = goboard.Move.pass_turn()
            elif human_move == 'resign':
                move = goboard.Move.resign()
            else:
                point = point_from_coords(human_move.strip())
                move = goboard.Move.play(point) 
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)


if __name__ == '__main__':
    main()
# end::play_against_your_bot[]