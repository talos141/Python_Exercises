
def board_size_h(size):
    h = " ---" * size
    return h

def board_size_v(size):
    v = " |  " * (size + 1)
    return v

def board_size_t(size):
    size_constant = size
    while size  > 0:
        print(" " + board_size_h(size_constant), end="\n")
        print(board_size_v(size_constant), end="\n")
        size -= 1
    print(" " + board_size_h(size_constant), end="\n")


if __name__ == "__main__":

    size = int(input("what size should the board be?"))

    board_size_t(size)


#Sample solution


    # def print_horiz_line():
    #     print(" --- " * board_size)
    #
    #
    # def print_vert_line():
    #     print("|   " * (board_size + 1))
    #
    #
    # if __name__ == "__main__":
    #     board_size = int(input("What size of game board? "))
    #
    #     for index in range(board_size):
    #         print_horiz_line()
    #         print_vert_line()
    #     print horiz_line(
    #