# Final Project Sevilla
class Transaction:
    # Class representing a financial transaction (parent class)

    def __init__(self, amount, category, date=None):
        self.__amount = amount  # Encapsulation: Private attribute (double underscore)
        self.__category = category  # Encapsulation: Private attribute
        self.__date = date if date else "Unknown"  # Default value handling

    # Getter methods provide controlled access to private attributes
    def get_amount(self):
        return self.__amount

    def get_category(self):
        return self.__category

    def get_date(self):
        return self.__date

    def display(self):
        # Overridable method in child classes 
        return f"{self.__date}: {self.__category} - ${self.__amount:.2f}"


# Expense class extends Transaction
class Expense(Transaction):
    # Represents an expense

    def __init__(self, amount, category, date=None):
        super().__init__(amount, category, date)  # Calling the parent class constructor

    def display(self):
        # Overriding the display method 
        return f"Expense - {super().display()}"


# Income class extends Transaction
class Income(Transaction):

    def __init__(self, amount, category, date=None):
        super().__init__(amount, category, date)  # Calling the parent class constructor

    def display(self):
        # Overriding the display method 
        return f"Income - {super().display()}"


class FinanceTracker:
     # Separate class to manage transactions

    def __init__(self):
        self.transactions = []  # Tracker maintains a list of transaction objects

    def add_transaction(self, transaction):
        # Encapsulation, Transactions are stored within the class
        self.transactions.append(transaction)

    def delete_transaction(self, index):
        # Handles deletion of transactions with validation
        if 0 <= index < len(self.transactions):
            self.transactions.pop(index)  # Remove transaction by index
            print("Transaction deleted successfully.")
        else:
            print("Invalid index.")

    def view_summary(self):

        total_income = sum(t.get_amount() for t in self.transactions if isinstance(t, Income))
        total_expense = sum(t.get_amount() for t in self.transactions if isinstance(t, Expense))
        balance = total_income - total_expense  # Simple financial calculation

        print("\nSummary Report:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Balance: ${balance:.2f}\n")

    def display_transactions(self):

        for i, t in enumerate(self.transactions):
            print(f"{i}. {t.display()}")  # Calls the overridden display method dynamically


# Entry point for the program
def main():
    tracker = FinanceTracker()  # Object creation

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
            date = input("Enter Expense Date: ")
            tracker.add_transaction(Expense(amount, category, date))  # Polymorphism: Using inherited class

        elif choice == "2":
            amount = float(input("Enter income amount: "))
            category = input("Enter category (Salary, Bonus, etc.): ")
            date = input("Enter Expense Date: ")
            tracker.add_transaction(Income(amount, category, date))  # Polymorphism: Using inherited class

        elif choice == "3":
            tracker.display_transactions()

        elif choice == "4":
            index = int(input("Enter transaction index / number to delete: "))
            tracker.delete_transaction(index)

        elif choice == "5":
            tracker.view_summary()

        elif choice == "6":
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()  # Starts the program execution
