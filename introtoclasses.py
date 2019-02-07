'''
creat a simple class
attributes - variables
methods - functions working usually with attributes
'''


class CashRegister:
    def __init__(self):
        self.items = 0
        self.price = 0

    def upgrade_register(self):
        self.items = self.items + 1
        self.price = self.price + price

    def display_register(self):
        return print('the number of items ', self.item, '\n the total price ', self.price)

    def clear_register(self):
        self.items = 0
        self.price = 0


register1 = [CashRegister]
register1.upgrade_register(1.95)
register1.upgrade_register(.65)
register1.upgrade_register(25000)
register1.display_register()

register2 = CashRegister()
print('register2')
register2.display_register()
register2.upgrade_register(500)
print(register2.price)

register1.clear_register()
register1.display_register()
