# size = input("what size should the board be?")


def board_size_h(size):
    h = " ---" * size
    return h

def board_size_v(size):
    v = " |  " * (size + 1)
    return v

def board_size_t(size):
    size_constant = size
    print(" " + board_size_h(size_constant), end="\n")
    print(board_size_v(size_constant), end="\n")





# print(board_size_v(3))

board_size_t(3)