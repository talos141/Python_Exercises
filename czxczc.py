# def board_graphic():
#     i = 0
#     grid = [["X", "O", "X"],
#             [" ", " ", " "],
#             [" ", " ", " "]]
#
#     h = " ---" * 3
#
#
#     while i < 3:
#         v = " | " + grid[i][0] + " | " + grid[i][1] + " | " + grid[i][2] + " | "
#         print(" " + h, end="\n")
#         print(v, end="\n")
#         i += 1
#     print(" " + h, end="\n")
#
# board_graphic()

from copy import deepcopy


def check_winner(board_row):


    for l in board_row:

        for n, x in enumerate(l):

            if x == "X":

                l[n] = 1

            elif x == "O":

                l[n] = 2

            elif x == " ":

                l[n] = 0


    i = 0

    board_col = [[], [], []]

    board_dig = [[board_row[0][0], board_row[1][1], board_row[2][2]], [board_row[0][2], board_row[1][1], board_row[2][0]]]

    board_t = [board_row, board_col, board_dig]

    while i != 3:
        for x in board_row:
            board_col[i].append(x[i])
        i += 1

    for block in board_t:

        for row in block:
            if sum(row) == 3 and len(set(row)) == 1:
                print("Player one won")
                exit()
            elif sum(row) == 6:
                print("Player two won")
                exit()
    else:
        print("no winner")



grid_check = []

grid = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

grid_check = deepcopy(grid)

check_winner(grid_check)
print(grid)
print(grid_check)

