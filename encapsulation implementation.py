class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling price : ",self.__maxprice)
    def set_Maxprice(self, price):
        self.__maxprice = price


dell = Computer()
dell.sell()
dell.__maxprice = 1000
dell.sell()
dell.set_Maxprice(1000)
dell.sell()