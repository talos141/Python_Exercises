birthday_dict = {"John Lennon": "9/10/1940",
                 "Albert Einstein": "14/3/1879",
                 "Ramana Maharshi": "30/12/1879"}

option = "\n".join(list(birthday_dict.keys()))

key = input("who would you like to know the birthday of out of these options:\n%s\n" % option)

print("the birthday of %s is %s" % (key, birthday_dict[key]))