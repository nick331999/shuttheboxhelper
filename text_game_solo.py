"""Solo test based shut the box game.
"""
import optimal_move as om 
import best_move_checker as bcm 
import random

choice_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,}
box = ['1','2','3','4','5','6','7','8','9']
possible_moves = []

def rolldice() -> int:
    return random.randint(1,6)

def box_ints(box) -> [int]:
    x = []
    for k in box:
        if k.isdigit():
            x.append(int(k))
    return x

def play_game(box) -> None:
    win = False
    while win == False:
        roll1 = rolldice()
        roll2 = rolldice()
        possible_moves = bcm.possible_moves(box_ints(box), roll1 + roll2)
        print(possible_moves, box, roll1 + roll2)
        if len(possible_moves) == 0:
            print('YOU LOSE')
            break
        if len(possible_moves) == 1:
            a = possible_moves[0]
            b = 'X'
            c = 'X'
            d = 'X'
            e = 'X'
            f = 'X'
        elif len(possible_moves) == 2:
            a = possible_moves[0]
            b = possible_moves[1]
            c = 'X'
            d = 'X'
            e = 'X'
            f = 'X'
        elif len(possible_moves) == 3:
            a = possible_moves[0]
            b = possible_moves[1]
            c = possible_moves[2]
            d = 'X'
            e = 'X'
            f = 'X'
        elif len(possible_moves) == 4:
            a = possible_moves[0]
            b = possible_moves[1]
            c = possible_moves[2]
            d = possible_moves[3]
            e = 'X'
            f = 'X'
        elif len(possible_moves) == 5:
            a = possible_moves[0]
            b = possible_moves[1]
            c = possible_moves[2]
            d = possible_moves[3]
            e = possible_moves[4]
            f = 'X'
        elif len(possible_moves) >= 6:
            a = possible_moves[0]
            b = possible_moves[1]
            c = possible_moves[2]
            d = possible_moves[3]
            e = possible_moves[4]
            f = possible_moves[5]

        print("=================================")
        print("||        SHUT THE BOX         ||")
        print("||                             ||")
        print("||    ",box[6],"      ",box[7],"      ",box[8],"    ||")
        print("||                             ||")
        print("||    ",box[3],"      ",box[4],"      ",box[5],"    ||")
        print("||                             ||")
        print("||    ",box[0],"      ",box[1],"      ",box[2],"    ||")
        print("||                             ||")
        print("=================================")
        print("||    ",roll1,"     ROLLS     ",roll2,"    ||")
        print("=================================")
        print("=================================")
        print("||           CHOICES           ||")
        print("|| a:",a," b:",b,
        " c:",c," d:",d," e:",
        e," f:",f,"\\\\")

        choice = input()
        move = possible_moves[choice_dict[choice]]
        for num in move:
            i = box.index(str(num))
            box[i] = 'X'
        if len(box) == 0:
            print('YOU SHUT THE BOX!!!!')
            win = True


play_game(box)