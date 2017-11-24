
def prime(number):
    num_list = range(2, number)
    check = False
    for x in num_list:
        if number % x == 0:
            print("this is not a prime")
            check = True
            break
    if check == False:
        print("its a prime")
               
num = int(input('give me a number'))

prime(num)        
        
    
