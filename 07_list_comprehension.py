a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = []

"""solution 1
for x in a:
    if x % 2 == 0:  b.append(x)

print (b)
"""

#solution 2:list comprehension :A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal:


b = [x for x in a if x % 2 == 0]

print(b)




b = [x for x in a if x % 2 == 0]

print(b)

