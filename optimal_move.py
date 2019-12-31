"""Calculates the optimal move using the optimal move table 
text file. Note thatthis variation always uses 2 dice. 
Move table copied from 
http://www.durangobill.com/ShutTheBoxExtra/STB2DICE.txt 
"""

BOX_NUMS = 9
THE_BOX = list(range(1, BOX_NUMS + 1))

def generate_optimal_move_dict(file: str) -> dict:
    """Generates a dictionary from the optimal moves table

    """
    final_dict = {}
    f = open(file, "r")
    line = f.readline()
    while line != '':
        line_array = line.split()
        final_dict[line_array[0]] = line_array
        line = f.readline()
    return final_dict

def get_optimal_move(available_nums: [int], roll: int, my_dict: dict) -> [int]:
    """Gets the optimal move for any 2 dice roll.
    Based on the optimal move table.

    """
    flipped_str = get_flipped(available_nums)
    optimal_move = my_dict[flipped_str][roll]
    return str_to_list(optimal_move)

def str_to_list(my_str: str) -> [int]:
    """Takes a string of numbers and converts
    it into a list of integers, where each
    digit is an element.
    """
    my_list = []
    for char in my_str:
        my_list.append(int(char))
    return my_list

def get_flipped(available_nums: [int]) -> str:
    """Gets flipped nums from available nums.
    Then sorts the nums and puts them into one string

    """
    flipped_nums = [1,2,3,4,5,6,7,8,9]
    flipped_str = ''
    for num in available_nums:
        if num in flipped_nums:
            flipped_nums.remove(num)
    for num in flipped_nums:
        flipped_str += str(num)
    if flipped_str == '':
        return '0'
    return flipped_str

#print(get_flipped( [2, 3, 4] ))
#print(get_flipped( [2, 3, 4,5] ))
#my_dict = generate_optimal_move_dict("optimal_move_table.txt")
#test_box = [1,2,3,4,5,6,7,8,9]
#print(get_optimal_move(test_box , 7, my_dict))
#print(get_optimal_move([1,2,3,4,5,6,9] , 7, my_dict))