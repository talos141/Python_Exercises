grid = [["", "", ""],
        ["", "", ""],
        ["", "", ""]]



def mark(x, y, type):

    grid[x][y] = str(type)
    print(grid)

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
                break

        if counter == 9:
            exit()

        while True:
            pl_two = input("Player two:please enter the column and row number in the format r,c:\n")

            if placement != "O" and placement != "X":
                mark(cordinates(pl_two)[0], cordinates(pl_two)[1], "O")
                counter += 1
                break


if __name__ == "__main__":


    run()










