#Below example shows how to access, update and delete static and instance variable

class foodMenu:
    '''This class prints food items ordered by customer.'''
    appName = 'Eatery'                        #Static Variable defined here
    Location = 'UK'
    def __init__(self,itemtype,name,dessert): #constructor of the class
        self.itemtype = itemtype              #instance variables defined here
        self.name = name
        self.dessert = dessert

    def myOrder(self):                        #It is instance method as it is accessing instance variables
        print("It is: ", self.itemtype)
        foodMenu.appName = 'Veg Eatery'       #Like this we can modify static variable, alternative way is cls.appName
        print("Order of: ", self.name)
        print("Want this dessert:", self.dessert)

    @classmethod                             #It is class method using static variable of the class
    def myApp(cls):
        print("Welcome to our famous food joint:", cls.appName)

    @staticmethod                           #It is static method not using any of static or instance variable of class
    def tips(t):
        print('Thank you for the tip $$ of', t)
        foodMenu.appName = 'Eatery'   #Modifying static variable in static method, we have to mandatorily use class name. Cannot use cls here
        print('Come again to', foodMenu.appName)
        del foodMenu.appName #Like this we can delete static variable

c1 = foodMenu('Veg','Veg Noodles', 'Vanilla icecream')
print("Welcome to ", foodMenu.appName) #we can access static variable using object reference also but it is recommended
c1.Location = 'India' #If instance variable of this name is not present it will add a new one
c1.myOrder()
print("Welcome to ", foodMenu.appName) #priority is given to instance variable of same name if it is present in method
print("We are located at", c1.Location) #static variable is UK but due to priority to instance variable if present in method it is showing India Location
del c1.Location #Here we are deleting instance variable, if we want to delete static variable then we have to use classname or cls.<varname>
c1.tips(10)
c2 = foodMenu('Non Veg', 'Fried Chicken','fruit cake')
print("We are located at", foodMenu.Location) #It will print value of static variable as instance var is not present