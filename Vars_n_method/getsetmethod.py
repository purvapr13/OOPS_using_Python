#Example to create getter and setter method. Primarily used for extra validations

class Balance:
    def __init__(self, bal=0):
        self.bal = bal

    def setBal(self, x):  #setter method, also called as mutator method
        if x<1 or x>100000000:
            print('Please enter the value withing limit of 1 to 100000000')
        else:
            self.bal = x

    def getBal(self): #getter method, also called as accessor method
        return self.bal

c1 = Balance()
mybal = c1.setBal(100)  #To set value using setter method
print(c1.getBal())      #To get value using getter method
mybal = c1.setBal(100000001)