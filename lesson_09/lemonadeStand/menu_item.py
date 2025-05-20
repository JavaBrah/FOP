
class MenuItem():
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price
    
    def getName(self):
        return self._name
    
    def getWholesaleCost(self):
        return self._wholesale_cost
    
    def getSellingPrice(self):
        return self._selling_price