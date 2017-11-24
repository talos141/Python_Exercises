a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89, 89]
c = []
for x in a:
    for y in b:
        if x == y:
            c.append(x)
print(list(set(c)))


#solution 2(better):

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89, 89]

for x in a:
    if x in b:
        c.append(x)
print(list(set(c)))


#solution 3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89, 89]
c = []



c = [x for x in a if x in b]

print(list(set(c)))