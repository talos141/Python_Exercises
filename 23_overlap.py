with open("happynumbers.txt", 'r') as open_file:
    happy_num = open_file.read().split("\n")


with open("primenumbers.txt", 'r') as open_file2:
    prime_num = open_file2.read().split("\n")

overlaplist = []

for x in happy_num:
    if x in prime_num:
        overlaplist.append(int(x))
print(overlaplist)


