number = int(input("type a number: "))
divisor = 2
while divisor <= number:
    if number % divisor == 0:
        print(divisor)
        divisor += 1

    else:
        divisor +=1