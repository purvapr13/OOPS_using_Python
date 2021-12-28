#Example of Has-A relationship(Composition)
class veg:
    def vegMenu(self):
        print('Only Veg Pulao is available in veg')
class nonveg:
    def nonvegMenu(self):
        print('only Chicken Biryani is available in non-veg')
class restaurant:
    def __init__(self):
        self.veg = veg()
        self.nonveg = nonveg()

    def overallMenu(self):
        print("welcome to Eatery, please look our menu here")
        self.veg.vegMenu()
        self.nonveg.nonvegMenu()

visit = restaurant()
visit.overallMenu()
