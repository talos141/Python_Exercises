# import random
#
# list_a = sorted([random.randint(0, 11) for x in range(0, 11)])
#
#
#
# def check(num):
#
#     if num in list_a:
#         return (True)
#     else:
#         return (False)
#
#
# number = int(input("enter number: \n"))
#
# print(check(number))


#solution 2

import random



def check(num, list_a):
    list_b = list_a

    if len(list_b) % 2 == 0:
        if list_b[len(list_b)-1] == num:
            return True
        else:
            list_b.remove(list_b[len(list_b)-1])

    while len(list_b) != 1:
        middle = (len(list_b) - 1) // 2

        if num > list_b[middle]:
            list_b = list_b[middle + 1::]

        elif num < list_b[middle]:

            list_b = list_b[0:middle]
        else:
            return True
            break
    else:
        if num == list_b[0]:
            return (True)
        else:
            return (False)



list_a = sorted(list(set([random.randint(0, 100) for x in range(0, 7)])))
print(list_a)
# list_a = [1, 2, 3, 4, 7, 8, 9, 10, 11]
# print(list_a)

number = int(input("enter number: \n"))

print(check(number, list_a))

