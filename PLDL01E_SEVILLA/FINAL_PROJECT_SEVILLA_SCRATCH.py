from datetime import datetime
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class Transaction:
    """Base class for financial transactions"""
    def __init__(self, amount, category, date=None):
        self.__amount = amount
        self.__category = category
        self.__date = date if date else datetime.now().strftime("%Y-%m-%d")

    def get_amount(self):
        return self.__amount

    def get_category(self):
        return self.__category

    def get_date(self):
        return self.__date

    def display(self):
        return f"{self.__date}: {self.__category} - ${self.__amount:.2f}"

class Expense(Transaction):
    """Represents an expense"""
    def __init__(self, amount, category, date=None):
        super().__init__(amount, category, date)

    def display(self):
        return f"Expense - {super().display()}"

class Income(Transaction):
    """Represents an income"""
    def __init__(self, amount, category, date=None):
        super().__init__(amount, category, date)

    def display(self):
        return f"Income - {super().display()}"

class FinanceTracker:
    """Manages transactions and summary reports"""
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def delete_transaction(self, index):
        if 0 <= index < len(self.transactions):
            self.transactions.pop(index)
            print("Transaction deleted successfully.")
        else:
            print("Invalid index.")

    def view_summary(self):
        total_income = sum(t.get_amount() for t in self.transactions if isinstance(t, Income))
        total_expense = sum(t.get_amount() for t in self.transactions if isinstance(t, Expense))
        balance = total_income - total_expense

        print("\nSummary Report:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Balance: ${balance:.2f}\n")

    def display_transactions(self):
        for i, t in enumerate(self.transactions):
            print(f"{i}. {t.display()}")

def main():
    clear_screen() # Clear the screen of the console
    tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Transactions")
        print("4. Delete Transaction")
        print("5. View Summary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter category (Food, Rent, etc.): ")
            tracker.add_transaction(Expense(amount, category))

        elif choice == "2":
            amount = float(input("Enter income amount: "))
            category = input("Enter category (Salary, Bonus, etc.): ")
            tracker.add_transaction(Income(amount, category))

        elif choice == "3":
            tracker.display_transactions()

        elif choice == "4":
            index = int(input("Enter transaction index to delete: "))
            tracker.delete_transaction(index)

        elif choice == "5":
            tracker.view_summary()

        elif choice == "6":
            print("Exiting... Have a financially sound day!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()