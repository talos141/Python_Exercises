num = int(input("enter fib list length"))


def fib(number):
    fiblist = [0, 1]
    if number == 0:
        fiblist = []
    elif number == 1:
        fiblist = [0]
    else:     
        for x in range(2, number+1):
            n = fiblist[x-1] + fiblist[x-2]
            fiblist.append(n)
    print(fiblist)        
        
    
fib(num)

