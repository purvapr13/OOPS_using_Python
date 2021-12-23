#This example showing use of inner class
class bank: #whenever bank class is created automatically branch class will be created
    bankn = 'PPB'
    def __init__(self):
        self.ifs = self.branch()
    def ifsc(self):
        ifsc = bank.bankn+self.ifs.code
        print('ifsc code is ', ifsc)
        self.ifs.brloc()  #as object is there we can call branch class functions here

    class branch:  #Inner class created
        def __init__(self):
            self.code = '413'

        def brloc(self):
            print("This branch is located in Punjab")

myBnk = bank()
myBnk.ifsc()
