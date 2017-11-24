import random


total = 0

while True:
    number = random.randint(1,9)

    
    
    a = int(input("Guess a number between one and nine:\n"))

    if a > number:
        print("you guessed too high")
    elif a < number:
        print("you guessed too low")
    else:
        print("you guessed right!")

    print(",the number was" + " " + str(number))

    input("would you like another try?") = b

    if b == "yes":
        total += 1
        continue

