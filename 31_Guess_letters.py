import random

with open('sowpods.txt', 'r') as open_file:
    line = open_file.readlines()
    while True:
        word = (line[random.randint(0, len(line))].strip("\n"))
        if len(word) <= 6:
            break

word = list(word)

out = ["_" for x in range(0, len(word))]

history = []

counter = 6

while out != word and counter > 0:
    while True:
        guess =  (input("take a guess: \n")).upper()
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
        print("incorrect guess you have %s lives left" % counter)
        counter -= 1

if counter == 0:
    print("you lost the word is- %s" % ("".join(word)).lower())
else:
    print("you won the word is- %s" % ("".join(word)).lower())