def placement():
    counter = 0

    grid = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]

    while counter != 9:



        pl_one = input("Player one:please enter the column and row number in the format r,c:\n")

        pl_one = (pl_one.split(","))
        x = int(pl_one[0]) -1
        y = int(pl_one[1]) - 1

        counter += 1

        grid[x][y] = "x"

        print(grid)

        pl_two = input("Player two:please enter the column and row number in the format r,c:\n")
        pl_two = (pl_two.split(","))

        x2 = int(pl_two[0]) -1
        y2 = int(pl_two[1]) - 1

        counter += 1

        grid[x2][y2] = "O"

        print(grid)

    else:
        exit()









placement()