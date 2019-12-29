
"""Checks the best move for a game of shut the box
"""

BOX_NUMS = 9


def best_move(available_nums: [int], roll: int) -> [int]:
    """Calculates the best move to guarantee the highest chance of
    survival on a 2 dice roll next turn.

    >>> best_move([1,2,3,4,5,6,7,8,9], 9)
    [9]
    >>> best_move(1,2,3,4,5,6,7,8], 10)
    [7, 3]

    """

    return None


def next_move_survival_probability(available_nums: [int]) -> int:
    """returns the probability of being able to stay in the game
    after rolling and taking next turn.

    >>> best_move([2,3])
    0.194
    >>> best_move(1,2,3,4,5,6])
    1

    """

    return None

def combinations_for_result(roll: int) -> int:
    """Returns the number of ways that a result can be
    achieved using 2 6 sided dice.

    >>> combinations_for_result(2)
    1
    >>> combinations_for_result(7)
    6

    """

    return None


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


def effective_array(available_nums) -> [int]:
    """Returns the elements of available_nums and all numbers below
    BOX_NUMS it sums to.
    >>> get_diff([1,2,3,4,5,6])
    [1,2,3,4,5,6,7,8,9]
    >>> get_diff([2,5,6,8,9])
    [2,5,6,7,8,9]

    """

    return None

def nums_that_sum_to(target: int) -> [[int]]:
    """Returns all the combinations of numbers less than BOX_NUMS
    that sum to target.
    >>> nums_that_sum_to(7)
    [[1,2,4], [3,4], [2,5], [7]]
    >>> nums_that_sum_to(3)
    [[1,2], [3]]

    """

    return None