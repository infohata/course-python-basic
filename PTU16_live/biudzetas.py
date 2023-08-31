from datetime import datetime
import os
import pickle
from logerius import logerius


def input_float(prompt, message="You must enter a number"):
    while True:
        try:
            value = float(input(prompt))
        except Exception as error:
            logerius.exception('Error: %s', error)
        else:
            return value


class Record:
    def __init__(self, amount: float, message: str) -> None:
        self.amount = amount
        self.message = message
        self.created_at = datetime.now()
    

class Income(Record):
    def __init__(self, amount: float, message: str, sender: str) -> None:
        super().__init__(amount, message)
        self.sender = sender


class Expense(Record):
    def __init__(self, amount: float, message: str, receiver: str) -> None:
        super().__init__(amount, message)
        self.receiver = receiver


class Budget:
    def __init__(self, filename="budget.pickle") -> None:
        self.filename = filename
        if os.path.exists(filename):
            with open(filename, "rb") as budget_file:
                self.ledger = pickle.load(budget_file)
        else:
            self.ledger = []

    def save(self, new_filename: str|None = None) -> None:
        filename = new_filename or self.filename
        with open(filename, "wb") as budget_file:
            pickle.dump(self.ledger, budget_file)

    def add_income(self) -> None:
        amount = input_float("Amount: ")
        sender = input("Sender: ")
        message = input("Message: ")
        income = Income(amount, message, sender)
        self.ledger.append(income)
        logerius.info(f"Added income of {income.amount} from {income.sender} with message {income.message}")

    def add_expense(self) -> None:
        amount = input_float("Amount: ")
        receiver = input("Receiver: ")
        message = input("Message: ")
        expense = Expense(amount, message, receiver)
        logerius.info(f"Added expense of {expense.amount} to {expense.receiver} with message {expense.message}")
        self.ledger.append(expense)

    @property
    def balance(self) -> float:
        total = 0.0
        for record in self.ledger:
            if type(record) == Income:
                total += record.amount
            elif type(record) == Expense:
                total -= record.amount
        return total
    
    def print_balance(self) -> None:
        print(f"Total | {self.balance:11.2f}")

    def print_ledger(self) -> None:
        for num, record in enumerate(self.ledger):
            if type(record) == Income:
                print(f"{num+1:5d} | +{record.amount:>10.2f} | {record.created_at} | {record.sender}\n\t{record.message}")
            elif type(record) == Expense:
                print(f"{num+1:5d} | -{record.amount:>10.2f} | {record.created_at} | {record.receiver}\n\t{record.message}")
        self.print_balance()


def run():
    budget = Budget("budget.pickle")
    menu = """
    ===========[ PTU16 Budget ]==========
    0 - get outta here
    1 - add income
    2 - add expenses
    3 - print ledger
    4 - print balance
    _____________________________________
    Make a choice which matters: """
    while True:
        choice = input(menu)
        if choice == "0":
            budget.save()
            break
        elif choice == "1":
            budget.add_income()
        elif choice == "2":
            budget.add_expense()
        elif choice == "3":
            budget.print_ledger()
        elif choice == "4":
            budget.print_balance()

if __name__ == '__main__':
    logerius.debug("it works!")
    run()
    logerius.debug("bye bye!")
