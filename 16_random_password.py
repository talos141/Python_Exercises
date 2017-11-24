import random
import string

numlist = [str(random.randint(0, 10)) for x in range(0, 11)]

print(numlist)

char = [x for x in (string.ascii_lowercase)]

char_u = [x for x in (string.ascii_uppercase)]

char_s = "!@#$%^&*"


print(char)

random.shuffle(char)

print(char)

comb = random.sample(char_u, 1) + random.sample(numlist, 4) + random.sample(char, 4) +random.sample(char_s, 2)

print(comb)
random.shuffle(comb)



print("".join(comb))         
