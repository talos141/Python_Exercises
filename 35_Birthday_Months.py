import json

from collections import Counter

months_names = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
          6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}


with open("birthday_dict.json", "r") as f:
    birthday_dict = json.load(f)

months = []
dash = "/"
for x in birthday_dict:

    x = birthday_dict[x]
    if len(x) == 9:
        if dash in x[1:2]:
            x = x[2:4]
        else:
            x = x[3:4]

    elif len(x) == 8:
        x = x[2:3]
    else:
        x = x[3:5]
    months.append(months_names[int(x)])


c = Counter(months)

for x in months:
    print("%s:%d" % (x, c[x]))
