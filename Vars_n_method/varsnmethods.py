#Below example showing use of instance, class and static method and variables

class foodMenu:
    '''This class prints food items ordered by customer.'''
    appName = 'Eatery'                        #Static Variable defined here
    def __init__(self,itemtype,name,dessert): #constructor of the class
        self.itemtype = itemtype              #instance variables defined here
        self.name = name
        self.dessert = dessert

    def myOrder(self):                        #It is instance method as it is accessing instance variables
        print("It is: ", self.itemtype)
        print("Order of: ", self.name)
        print("Want this dessert:", self.dessert)

    @classmethod                             #It is class method using static variable of the class
    def myApp(cls):
        print("Welcome to our famous food joint:", cls.appName)

    @staticmethod                           #It is static method not using any of static or instance variable of class
    def tips(t):
        print('Thank you for the tip $$ of', t)


c1 = foodMenu('Veg','Veg Noodles', 'Vanilla icecream')
c1.myOrder()
c1.myApp()
c1.tips(10)
c2 = foodMenu('Non Veg', 'Fried Chicken','fruit cake')
c2.myOrder()
