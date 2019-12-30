"""A bot to play games of shut the box
"""
from typing import Dict
import best_move_checker as bmc
import random

BOX_NUMS = 9
THE_BOX = list(range(1, BOX_NUMS + 1))
DICE = 2
DICE_SIDES = 6
DICE_VALUES = list(range(1, DICE_SIDES + 1))
DUMB = 'DUMB'
SMART = 'SMART'
RANDOM = 'RANDOM'

def game_simulator(starting_box: [int], bot_type: str, num_games: int) -> float:
    """Plays num_games games with using starting_box and bot_type.
    Then, the winrate over all games is returned as a float.

    """
    total_wins = 0
    for i in range(num_games):
        total_wins += play_game(starting_box, bot_type)
    return total_wins / num_games

def play_game(starting_box: [int], bot_type: str) -> int:
    """Plays a game of shutthebox, returns 1 if the box
    is shut, returns 0 if the box doesn't shut

    """
    my_box = starting_box
    while len(my_box) > 0:
        roll = make_roll()
        my_move = choose_move(my_box, bot_type, roll)
        if not my_move:
            return 0
        else:
            my_box = bmc.box_after_move(my_box, my_move)
    return 1

def make_roll() -> int:
    """Makes a roll from the available number of dice.

    """
    roll1 = DICE_VALUES[random.randint(0, len(DICE_VALUES) - 1)]
    roll2 = DICE_VALUES[random.randint(0, len(DICE_VALUES) - 1)]
    return roll1 + roll2

def choose_move(box: [int], my_type: str, roll: int) -> [int]:
    """Chooses a move depending on the type. The possible
    types are listed below.
    DUMB: makes only suboptimal moves
    SMART: makes the best moves
    RANDOM: makes random moves

    """
    possible_moves = bmc.possible_moves(box, roll)
    best_moves = bmc.best_moves(box, roll)
    if len(possible_moves) == 0:
        return []
    if my_type == RANDOM:
        return possible_moves[random.randint(0, len(possible_moves) - 1)]
    if my_type == SMART:
        return best_moves[0]
    if my_type == DUMB:
        dumb_moves = bmc.get_diff(possible_moves, best_moves)
        if dumb_moves:
            return dumb_moves[random.randint(0, len(dumb_moves) - 1)]
        else:
            return possible_moves[random.randint(0, len(possible_moves) - 1)]
