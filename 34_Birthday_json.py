

#writing json file
# #birthday_dict = {"John Lennon": "9/10/1940",
#                  "Albert Einstein": "14/3/1879",
#                  "Ramana Maharshi": "30/12/1879"}

# with open("birthday_dict.json", "w") as f:
#     json.dump(birthday_dict, f)

import json

with open("birthday_dict.json", "r") as f:
    birthday_dict = json.load(f)

option = "\n".join(list(birthday_dict.keys()))

key = input("who would you like to know the birthday of out of these options:\n%s\n" % option)

print("the birthday of %s is %s" % (key, birthday_dict[key]))