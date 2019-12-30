
"""Checks the best move for a game of shut the box
"""
from typing import Dict

BOX_NUMS = 9


def best_move(available_nums: [int], roll: int) -> str:
    """Calculates the best move to guarantee the highest chance of
    survival on a 2 dice roll next turn.

    >>> best_move([1,2,3,4,5,6,7,8,9], 9)
    [9]
    >>> best_move(1,2,3,4,5,6,7,8], 10)
    [7, 3]

    """
    move_dict = {}
    my_possible_moves = possible_moves(available_nums, roll)
    for i in range(len(my_possible_moves)):
        if (next_move_survival_probability(box_after_move(available_nums, my_possible_moves[i]))) in move_dict:
            move_dict[(next_move_survival_probability(box_after_move(available_nums, my_possible_moves[i])))].append(my_possible_moves[i])
        else:
            move_dict[(next_move_survival_probability(box_after_move(available_nums, my_possible_moves[i])))] = [(my_possible_moves[i])]
    max_key = max(move_dict.keys())
    best_sums = [move_dict[max_key]]
    print(move_dict)
    return best_sums[0]


def next_move_survival_probability(available_nums: [int]) -> int:
    """returns the probability of being able to stay in the game
    after rolling and taking next turn.

    >>> next_move_survival_probability([2,3])
    0.194
    >>> next_move_survival_probability(1,2,3,4,5,6])
    1

    """
    total_prob = 0
    if len(available_nums) > 0:
        for num in effective_array(available_nums, 12):
            total_prob += combinations_for_result(num)
    return total_prob / 36

def combinations_for_result(roll: int) -> int:
    """Returns the number of ways that a result can be
    achieved using 2 6 sided dice.

    >>> combinations_for_result(2)
    1
    >>> combinations_for_result(7)
    6

    """
<<<<<<< HEAD
    return -(abs(7 - roll)) + 6

=======
	return (-(abs(roll - 7)) + 6)
>>>>>>> 42ae584af45656e4aa8f91a3e13e6722e94a9add

def get_diff(arr1: [int], arr2: [int]) -> [int]:
    """Returns the elements which are not in common between
    two arrays of ints.
    >>> get_diff([1,2,3,4], [2,3,4,5])
    [1,5]
    >>> get_diff([6,7,9],[4,5,6,7,9])
    [4,5]

    """
    difference_array = []
    for num in arr1:
        if num not in arr2:
            difference_array.append(num)
    for num in arr2:
        if num not in arr1:
            difference_array.append(num)
    return difference_array


def effective_array(available_nums: int, cap: int) -> [int]:
    """Returns the elements of available_nums and all numbers below
    BOX_NUMS it sums to.
    >>> get_diff([1,2,3,4,5,6])
    [1,2,3,4,5,6,7,8,9]
    >>> get_diff([2,5,6,8,9])
    [2,5,6,7,8,9]

    """
<<<<<<< HEAD
    starting_list = []
    for num1 in available_nums:
        for num2 in available_nums:
            if num1 != num2:
                starting_list.append(num1 + num2)
    for num1 in available_nums:
        for num2 in available_nums:
            for num3 in available_nums:
                if num1 != num2 and num1 != num3 and num2 != num3:
                    starting_list.append(num1 + num2 + num3)
    final_list = available_nums
    for num in starting_list:
        if num not in final_list and num <= cap:
            final_list.append(num)      
    return final_list
=======
	
	return None
>>>>>>> 42ae584af45656e4aa8f91a3e13e6722e94a9add

def nums_that_sum_to(target: int) -> [[int]]:
    """Returns all the combinations of numbers less than BOX_NUMS
    that sum to target.
    >>> nums_that_sum_to(7)
    [[1,2,4], [3,4], [2,5], [7]]
    >>> nums_that_sum_to(3)
    [[3], [1, 2]]

    """
    nums_that_sum = []
    pool = list(range(BOX_NUMS + 1))[1:]
    if target <= BOX_NUMS:
        nums_that_sum.append([target])
    if target >= 2:
        for num1 in pool:
            for num2 in pool:
                if num1 + num2 == target and num1 != num2:
                    appender = [num1, num2]
                    appender.sort()
                    nums_that_sum.append(appender)
    if target >= 6:
        for num1 in pool:
            for num2 in pool:
                for num3 in pool:
                    if (num1 + num2 + num3 == target and 
                        not (num1 == num2 or num2 == num3 
                        or num3 == num1)):
                        appender = [num1, num2, num3]
                        appender.sort()
                        nums_that_sum.append(appender)
    if target >= 10:
        for num1 in pool:
            for num2 in pool:
                for num3 in pool:
                    for num4 in pool:
                        if (num1 + num2 + num3 + num4 == target and 
                            not (num1 == num2 or num2 == num3 or
                            num3 == num1 or num1 == num4 or 
                            num2 == num4 or num3 == num4)):
                            appender = [num1, num2, num3, num4]
                            appender.sort()
                            nums_that_sum.append(appender)
    final_list = []
    for element in nums_that_sum:
        if element not in final_list:
            final_list.append(element)
    return final_list

def box_after_move(available_nums: [int], move: [int]) -> [int]:
    """Removes all numbers from the array move. Then returns
    the box after these numbers have been removed.
    >>> box_after_move([1,2,3,4,5,6], [2,6])
    [1,3,4,5]
    >>> box_after_move([2,5,6,8], [2,8])
    [5,6]

    """
    final_list = []
    move_tester = move
    for i in move_tester:
        if i in available_nums:
            move_tester.remove(i)
    if len(move_tester) == 0:
        for num in available_nums:
            if num not in move:
                final_list.append(num)
        return final_list
    return []

def possible_moves(available_nums: [int], roll: int) -> [[int]]:
    """Returns all possible moves that can be made with
    the available numbers. A move is when a list of numbers
    are shut in the box.
    >>> possible_moves([1,3,6], 4)
    [[1,3]]]
    >>> possible_moves([1,2,3,4,6], 6)
    [[6], [2, 4], [1, 2, 3]]

    """
    final_moves = nums_that_sum_to(roll)
    for each_sum in final_moves:
        for num in each_sum:
            if num not in available_nums and each_sum in final_moves:
                final_moves.remove(each_sum)      
    return final_moves

def average_survival(available_nums: [int]) -> float:
    """Returns the average probability of survival given
    over all rolls for available nums.

    """
    total_prob = 0.0
    for i in range(11):
        total_prob += next_move_survival_probability(box_after_move(available_nums, (best_move(available_nums, i+2)[0])))
    my_prob = total_prob / 11
    return my_prob

def best_move_overall(available_nums: [int], moves: [[int]]) -> [int]:
    """Returns the best move while taking into account
    the next move.

    """
    print(moves)
    for move in moves:
        print(box_after_move(available_nums, move))
        print(average_survival(box_after_move(available_nums, move)))
    return None

#print(best_move([1,2,3,4,5,6,7,8], 9))
##print(effective_array([1,2,3,4,5,6]), BOX_NUMS)
#print(combinations_for_result(6))
#print(possible_moves([1,2,3,4,6], 6))
#print(next_move_survival_probability([]))
#print(average_survival([1,2,3,6,7,8]), "BREAK", average_survival([1,3,4,5,6,7]))
print(average_survival([2]))
#print(best_move([1,2,3,4,5], 5))
#print(best_move_overall([1,2,3,4,5],best_move([1,2,3,4,5], 5)))
