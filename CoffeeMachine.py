import time

class CoffeeMachine():
    def __init__(self, menu, resources):
        self.menu = menu
        self.res = resources
        self.profit = 0
    
    def show_profit(self):
        return f'Money in the machine: {self.profit}€'
    
    def show_menu(self):
        menu_string = "Menu:\n"
        for item in self.menu:
            item_cost = self.menu[item]['cost']
            menu_string += f'{item} : {item_cost}€\n'
        return menu_string

    def show_report(self):
        report_string = "Available resources:\n"
        for item in self.res:
            report_string += f'{item} : {self.res[item]} g\n'
        return report_string
    
    def check_resources(self, choice):
        for item in self.menu[choice]['ingredients']:
            if self.menu[choice]['ingredients'][item] > self.res[item]:
                return False
        
        return True
    
    def process_coins(self):
        print('Please insert coins.')
        total = 0
        values = [0.1, 0.2, 0.5, 1, 2]
        print()
        for value in values:
            coin = int(input(f'How many {value}€ coins would you like to add? '))
            total += value*coin
        print()
        return total
    
    def is_payment_sucessful(self, choice, payment):
        if payment >= self.menu[choice]['cost']:
            self.profit += self.menu[choice]['cost']
            change = payment - self.menu[choice]['cost']
            message = f"Here is your change: {change}€." if change != 0 else ""
            return True, message
        else:
            return False, "Not sufficient money!"

    def get_cost(self, choice):
        cost = self.menu[choice]['cost']
        return f'The {choice} costs {cost}€.'
        
    def make_coffee(self, choice):
        #print('Processing...')
        #time.sleep(3)
        for item in self.menu[choice]['ingredients']:
            self.res[item] -= self.menu[choice]['ingredients'][item]
        
        return f'Here is your {choice} ☕'
        
    def get_coffee(self, choice):
        if self.check_resources(choice):
            self.get_cost(choice)
            if self.is_payment_sucessful(choice, self.process_coins()):
                self.make_coffee(choice)