from __future__ import print_function
# tag::bot_vs_bot[]
from code.dlgo import goboard, gotypes
from code.dlgo.utils import print_board, print_move
from code.dlgo.scoring import compute_game_result
import time


def main():
    board_size = 0
    while not 5 <= board_size <= 19:
        board_size = int(input("Enter Board Size (5X5 - 19X19) : "))

    game_state = goboard.GameState.new_game(int(board_size))
    bots = {
        gotypes.Player.black: code.dlgo.agent.naive.RandomBot(),
        gotypes.Player.white: code.dlgo.agent.naive.RandomBot(),
    }
    while not game_state.is_over():
        time.sleep(0.5)  # <1>

        print(chr(40) + "[2J")  # <2>
        print_board(game_state.board)
        bot_move = bots[game_state.next_player].select_move(game_state)
        print_move(game_state.next_player, bot_move)
        game_state = game_state.apply_move(bot_move)

    game_result = compute_game_result(game_state)
    white_score = game_result.w + game_result.komi
    print("\n")
    print('white score: {}'.format(white_score))
    print('black score: {}'.format(game_result.b))
    print('{} wins with margin: {}'.format(game_result.winner, game_result.winning_margin))


if __name__ == '__main__':
    main()

# <1> We set a sleep timer to 0.5 seconds so that bot moves aren't printed too fast to observe
# 2. Before each move we clear the screen. The board is always printed to the same position on the command line.
# end::bot_vs_bot[]
