import random

def maximum(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z

a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)

print(maximum(a,b,c))