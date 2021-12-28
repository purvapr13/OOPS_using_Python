#Simple Example of Is-A Relationship (Inheritance)
class eatery:
    def comMenu(self):
        print('Today Everyone will get complimentory Cheese Cake')

class veg(eatery):
    def vegMenu(self):
        print('Only veg Fried Rice is available right now')

visit = veg()
visit.comMenu()
visit.vegMenu()
