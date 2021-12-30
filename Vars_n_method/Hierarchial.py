#single parent multiple child, Hierarchial Inheritance
class ppbank:
    def __init__(self):
        self.ifscode = 'ppb'

class ppbankUK(ppbank):
    def ukcode(self):
        self.code = '223'
        print('ifsc code for uk location is', self.ifscode+self.code)

class ppbankUS(ppbank):
    def uscode(self):
        self.code = '387'
        print('ifsc code for us location is', self.ifscode + self.code)

o1 = ppbankUK()
o1.ukcode()
o2 = ppbankUS()
o2.uscode()

