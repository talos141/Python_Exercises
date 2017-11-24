import random

if __name__=="__main__":

    def guess():
        number = str(random.randint(1000, 10000))
        # number = str(1234)
        cows = 0
        guess_num = 0
        
        while cows < 4:
            guess = input("guess a 4 digit number: \n")
            cows = 0
            bulls = 0
            for x, y in zip(guess, number):
                if y == x:
                    cows += 1
                else:
                    bulls += 1
            print("%s cows, %s bulls" % (cows, bulls))
            guess_num += 1

        if guess_num == 1:
            print("you have won on your first guess")

        else:
            print("you have won after %s guesses" % (guess_num))



guess()
