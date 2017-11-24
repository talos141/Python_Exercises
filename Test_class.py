class MaxSizeList(object):
    self.max_size = size

    def __init__(self, size):self.list_a = []

    def push(self, value):
        self.list_a.append(value)
        if len(self.list_a) > self.max_size:
            self.list_a.pop(0)
    def get_list(self):
        return self.list_a[0:self.max_size]

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("u")
b.push("let's")
b.push("go")


print(a.get_list())
print(b.get_list())




5j