import random

list1 = [random.randint(0, 10) for x in range(1, random.randint(0,9))]
print(list1)

def sets(l):
    return set(l)

def sets2(l):
    list2 = []
    for x in l:
        if x not in list2:
            list2.append(x)
    return list2        
        


print(sets(list1))

print(sets2(list1))




