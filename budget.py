class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        output = self.name.center(30, '*') + '\n'
        for item in self.ledger:
            output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount" : amount, "description" : description})
        '''
        A `deposit` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of `{"amount": amount, "description": description}`.
        '''
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount" : -amount, "description" : description})
            return True
        else:
            return False
        '''
        A `withdraw` method that is similar to the `deposit` method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return `True` if the withdrawal took place, and `False` otherwise.
        '''

    def get_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
        return total_cash
        '''
        A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        '''

    def transfer(self, amount, dest_budget_category):
        if self.check_funds(amount) is True:
            self.withdraw(amount, f"Transfer to {dest_budget_category.name}")
            dest_budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        '''
        A `transfer` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return `True` if the transfer took place, and `False` otherwise.
        '''
        

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
        '''
        A `check_funds` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method should be used by both the `withdraw` method and `transfer` method.
        '''

def create_spend_chart(categories):
    '''
    `create_spend_chart` takes a list of categories as an argument. It returns a string that is a bar chart.
    '''
    category_names = []
    spent_list = []
    spent_percentages = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:      #the withdraw is stored in the ledger as a negative amount
                total -= item['amount']
        spent_list.append(round(total, 2))
        category_names.append(category.name)
    
    for amount in spent_list:
        spent_percentages.append(round(amount / sum(spent_list), 2)*100)
    
    graph = "Percentage spent by category\n"

    labels = range(100, -10, -10)

    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:    
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"
    
    graph += "    ----" + ("---" * (len(category_names) - 1))
    graph += "\n     "

    longest_name_length = 0
    for name in category_names:
        if longest_name_length < len(name):
            longest_name_length = len(name)
    
    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length-1:
            graph += "\n     "
    
    return graph

    
