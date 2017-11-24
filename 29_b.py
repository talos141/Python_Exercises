
from copy import deepcopy

def board_graphic(grid_graphic):

    i = 0

    h = " ---" * 3

    while i < 3:
        v = " | " + grid_graphic[i][0] + " | " + grid_graphic[i][1] + " | " + grid_graphic[i][2] + " | "
        print(" " + h, end="\n")
        print(v, end="\n")
        i += 1
    print(" " + h, end="\n")



grid = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]


def mark(x, y, type):

     grid[x][y] = str(type)


def cordinates(string):
    string = (string.split(","))
    x1 = int(string[0]) - 1
    y1 = int(string[1]) - 1
    return x1, y1

def run():

    counter = 0


    while True:

        while True:
            pl_one = input("Player one:please enter the column and row number in the format r,c:\n")

            placement = grid[cordinates(pl_one)[0]][cordinates(pl_one)[1]]

            if  placement != "O" and placement != "X":

                mark(cordinates(pl_one)[0], cordinates(pl_one)[1], "X")
                counter += 1
                board_graphic(grid)
                grid_check = deepcopy(grid)
                check_winner(grid_check)

                break


        if counter == 9:
            break

        while True:
            pl_two = input("Player two:please enter the column and row number in the format r,c:\n")

            if placement != "O" and placement != "X":
                mark(cordinates(pl_two)[0], cordinates(pl_two)[1], "O")
                counter += 1
                board_graphic(grid)
                grid_check = deepcopy(grid)
                check_winner(grid_check)

                break


    if check_winner(grid) == True:
        print("it's a tie")

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
                print("Player one it the winner")
                exit()
            elif sum(row) == 6:
                print("Player one it the winner")
                exit()
    else:
        return True





if __name__=="__main__":
    run()