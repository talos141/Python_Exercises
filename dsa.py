

def check_winner(board):
    i = 0

    board_col = [[], [], []]

    board_dig = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]

    board_t = [board, board_col, board_dig]

    while i != 3:
        for x in board:
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




if __name__ == "__main__":

    game = [[1, 2, 0],
			[2, 2, 0],
			[2, 2, 2]]

    check_winner(game)