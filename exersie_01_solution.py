name = input("What is your name: ")
age = int(input("How old are you: "))
number = int(input("enter how many time the answer will repeat"))
year = str((2014 - age)+100)


print(((name + " will be 100 years old in the year " + year ) + "\n") * number)