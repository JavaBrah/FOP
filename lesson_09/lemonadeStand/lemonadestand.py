from lemonade_stand_exceptions import InvalidSalesItemError
class LemonadeStand():
    def __init__(self, name):
        self._name = name
        self.current_day = 0
        self.menu = {}
        self.sales_record = []

    def getName(self):
        return self._name
    
    def add_menu_item(self, menu_item):
        self.menu[menu_item.getName()] = {'Wholesale Cost': menu_item.getWholesaleCost(),
                                           'Selling Price': menu_item.getSellingPrice()}
    
    def enter_sales_for_today(self, sales: dict):
        todays_sales = {}
        try:
            for key in sales:
                if key in self.menu and key not in todays_sales:
                    todays_sales[key] = 1
                elif key in self.menu and key in todays_sales:
                    todays_sales[key] += 1
                else:
                    raise InvalidSalesItemError
        except InvalidSalesItemError:
            print(f"{InvalidSalesItemError}Item not on the menu")
