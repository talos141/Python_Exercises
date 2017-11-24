

options = [x for x in range(1, 101)]

start_index = 0

end_index = (len(options))

while True:

    options = options[start_index:end_index]

    middle = (len(options) - 1) // 2

    comp_guess = print("is your number %s ?" % options[middle])

    user_answer = input("answer high low or equal: \n")

    if user_answer == "=":
        print("Computer wins!")
        break

    elif user_answer == "+":
        start_index = middle + 1

    elif user_answer == "-":
        start_index = 0
        end_index = middle
