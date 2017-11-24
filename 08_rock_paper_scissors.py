#rock paper scissors:
a = "rock"

b = "scissors"

c = "paper"

def player_one():
    print("player one is the winner")

def player_two():
    print("player two is the winner")

def tie():
    print("It's a tie!")
    
while exit != "no":
        one = input("1:whats your choice?: \n")
    while two != a or b or c:
        two = input("2:whats your choice?: \n")
    if one = two:
        tie()
    if one == a:
        if two == b:
            player_one()
        elif two == c:
            player_two()
    elif one == b:
        if two == a:
            player_two()
        elif two == c:
            player_one()     
    else:
        if two == a:
            player_one()
        elif two == b:
            player_two()

    exit = input("would you like to play again-type yes or no?: \n")

    
    
