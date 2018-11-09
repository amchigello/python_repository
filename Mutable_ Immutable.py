# What I expected: [1, 2], [2, 3], [1, 2]
# What I got: [1, 2], [2, 3], [2, 3]

# Think this is because lists are a mutable type(able to change in place). So the += permanently changed a within the namespace of f.
# In other words the argument[1, 2] is stored in the namespace of f
# and even though it was changed externally(from somewhere else) that change still persists on it even without return.


class Test:
    def add_one(self, x):
        x[0] += 1
        x[1] += 1
        return x

    def add_one_tuple(self, x):
        return (x[0] + 1, x[1] + 1)

    def add_one_more(self, x):
        x += 1
        return x

    def f(self, a):
        print (a)
        print (self.add_one(a))
        print (a)

    def f1(self, a):
        print (a)
        print (self.add_one_more(a))
        print (a)

    def f3(self, a):
        print (a)
        print (self.add_one_tuple(a))
        print (a)


t = Test()
t.f([1, 2])
print("---------------")
t.f3((1, 2))
