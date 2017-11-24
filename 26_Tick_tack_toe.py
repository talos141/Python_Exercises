

def check_winner(board_row):
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
        exit()



if __name__ == "__main__":

    game = [[2, 0, 2],
			[1, 2, 0],
			[2, 0, 1]]

    check_winner(game)