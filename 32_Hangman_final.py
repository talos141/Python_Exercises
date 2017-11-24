









word = ["E", "V", "A", "P", "O", "R", "A", "T", "E"]

out = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

history = []

while out != word:
    while True:
        guess =  input("take a guess: \n")
        if guess not in history:
            break
        else:
            print("you have already tried that dummy")
    history.append(guess)
    i = 0

    if guess in word:

        for x in word:
            if x == guess:
                out[i] = x
            i += 1
        print(" ".join(out))

    else:
        print("incorrect guess")


else:
    print("you won the word is -  %s" % ("".join(out)).lower())