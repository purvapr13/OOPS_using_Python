#simple example of multilevel inheritance
class flour:
    def variety(self):
        print('Its wheat flour')

class bread(flour):
    def breadtype(self):
        print('its wheat flour bread')

class pizza(bread):
    def pizzaready(self):
        print('your pizza is ready with thin crust wheat-bread')

o1 = pizza()
o1.variety()
o1.breadtype()
o1.pizzaready()