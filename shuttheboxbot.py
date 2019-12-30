"""A bot to play games of shut the box
"""
from typing import Dict
import best_move_checker as bmc
import random
import optimal_move as om

BOX_NUMS = 9
THE_BOX = list(range(1, BOX_NUMS + 1))
DICE = 2
DICE_SIDES = 6
DICE_VALUES = list(range(1, DICE_SIDES + 1))
DUMB = 'DUMB'
SMART = 'SMART'
RANDOM = 'RANDOM'
OPTIMAL = 'OPTIMAL'

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
        print(my_box, 'ROLL: ',roll,'    MOVE: ', my_move)
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
    if my_type == OPTIMAL:
       # print('OPTIMAL:', box, "=======", roll)
        return om.get_optimal_move(box, roll, my_dict)

def compare_best_moves(available_nums: [int], roll: int, bot_type: str, num_sims: int) -> None:
    print("-=-=-=-=-=BEST MOVES=-=-=-=-=-")
    for move in bmc.best_moves(available_nums, roll):
        print("After ", move, " move ", game_simulator(bmc.box_after_move(available_nums, move), bot_type, num_sims))
    print("-=-=-=-=-=SUB-OPTIMAL MOVES=-=-=-=-=-")
    for move in bmc.get_diff(bmc.best_moves(available_nums, roll), bmc.possible_moves(available_nums, roll)):
        print("After ", move, " move ", game_simulator(bmc.box_after_move(available_nums, move), bot_type, num_sims))
    return None
#print(make_roll())
#print(THE_BOX)
#print(game_simulator([1,2,3,4,5,6,7,8,9], SMART, 1000))
my_dict = om.generate_optimal_move_dict("optimal_move_table.txt")
print(game_simulator([1,2,3,4,5,6,7,8,9], OPTIMAL, 1))
#print(game_simulator([1,2,3,4,5,6,7,8,9], OPTIMAL, 100))
#print("after [3,9] move " ,game_simulator([1,2,3,4,5,6,7,8,9], RANDOM, 1000))
#print("after [4,8] move " ,game_simulator([1,2,3,5,6,7,9], SMART, 1000))
#print("after [5,7] move " ,game_simulator([1,2,3,4,6,8,9], SMART, 1000))
#print("after [1,5,6] move " ,game_simulator([2,3,4,7,8,9], SMART, 1000))
#print("after [1,2,3,6] move " ,game_simulator([4,5,7,8,9], SMART, 1000))
#compare_best_moves([2,3,5,6,7,9], 8, RANDOM, 999)
#compare_best_moves([2,3,5,6,7,9], 8, OPTIMAL, 999)
#print(om.get_optimal_move( [2,4,5,6] , 7 ))