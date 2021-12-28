#when a function is required repeatedly only in a particular method then we can create nested method
# it increases code modularity also for data encapsulation
class solve:
    def subtract(self, a,b):
        def conditions(a,b):
            if a>b:
                print("a is greater than b and difference is ", a-b)
            else:
                print("This subtraction not required")
        conditions(a,b)

obj1 = solve()
obj1.subtract(3,4)
obj1.subtract(8,3)
