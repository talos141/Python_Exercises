import random
rl = random.randint(1, 9)
list_a = [random.randint(1, 9) for x in range(0, rl)]
print(list_a)


def fl(L):
    L2 = []    
    L2.append(L[0])
    L2.append(L[len(L)-1])
    print(L2)         
          
fl(list_a)    
    
              
              
