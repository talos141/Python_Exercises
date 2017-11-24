import random

with open('sowpods.txt', 'r') as open_file:
    line = open_file.readlines()
    print(line[random.randint(0, len(line))])



with open('sowpods.txt') as f:
	words = list(f)
print(random.choice(words).strip())
