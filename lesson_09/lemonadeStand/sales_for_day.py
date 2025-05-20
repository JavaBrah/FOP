
class SalesForDay():
    def __init__(self, number_of_days, sales_dictionary):
        self._number_of_days = number_of_days
        self._sales_dictionary = sales_dictionary

    def getNumberOfDays(self):
        return self._number_of_days
    
    def getSalesDictionary(self):
        return self._sales_dictionary
        