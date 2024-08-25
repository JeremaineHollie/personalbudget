class BudgetCategory:
    def __init__(self, name, allocated_budget):
        # Initialize private attributes
        self.__category_name = name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, name):
        self.__category_name = name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget
    def set_allocated_budget(self, amount):
        if amount > 0:
            self.__allocated_budget = amount
            self.__remaining_budget = amount
        else:
            print("Allocated budget must be a positive number.")

    # Method to add expense
    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"Expense of {amount} added. Remaining budget: {self.__remaining_budget}.")
            else:
                print("Expense exceeds remaining budget.")
        else:
            print("Expense amount must be a positive number.")

    # Method to display category summary
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")

# Example usage
if __name__ == "__main__":
    # Create a BudgetCategory instance
    food_category = BudgetCategory("Food", 500)

    # Add an expense
    food_category.add_expense(100)

    # Display category summary
    food_category.display_category_summary()
