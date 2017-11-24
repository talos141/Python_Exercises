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

# list_a = sorted([random.randint(0, 11) for x in range(0, 11)])



def check(num):
    list_a = [1, 3, 5, 30, 42, 43, 500]

    check_b = False

    while check_b == False and len(list_a) != 1:
        middle = (len(list_a) - 1) // 2

        if num > list_a[middle]:
            list_a = list_a[middle + 1::]

        elif num < list_a[middle]:

            list_a = list_a[0:middle]
        else:
            check_b = True

    if check_b == True:
        return (True)
    else:
        return (False)



number = int(input("enter number: \n"))

print(check(number))

