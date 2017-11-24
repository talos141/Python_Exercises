

def check_winner(board_row):
    i = 0

    board_col = [[number for number in group] for group in board_row]

    print(board_col)

    board_dig = [[board_row[0][0], board_row[1][1], board_row[2][2]], [board_row[0][2], board_row[1][1], board_row[2][0]]]

    board_t = [board_row, board_col, board_dig]


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