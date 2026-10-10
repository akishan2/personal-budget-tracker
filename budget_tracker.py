
import json
import os

filename = "budget_data.json"

# Load saved data
if os.path.exists(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    budget = data["budget"]
    expenses = data["expenses"]
else:
    budget = 0
    expenses = []


# Save budget and expenses
def save_data():
    with open(filename, "w") as file:
        json.dump(
            {
                "budget": budget,
                "expenses": expenses
            },
            file,
            indent=4
        )


print("=== PERSONAL BUDGET TRACKER ===")

while True:
    print("\n1. Set Monthly Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Show Remaining Budget")
    print("5. Exit")
    print("6. View Category Summary")

    choice = input("Enter your choice (1-6): ")

    # Set monthly budget
    if choice == "1":
        try:
            new_budget = float(
                input("Enter monthly budget: ₹")
            )

            if new_budget < 0:
                print("Budget cannot be negative.")
            else:
                budget = new_budget
                save_data()
                print("Budget saved successfully!")

        except ValueError:
            print("Please enter a valid number.")

    # Add expense
    elif choice == "2":
        name = input("Enter expense name: ").strip()
        category = input("Enter category: ").strip()

        if not name or not category:
            print("Expense name and category cannot be empty.")
            continue

        try:
            amount = float(
                input("Enter expense amount: ₹")
            )

            if amount <= 0:
                print("Expense must be greater than zero.")
            else:
                expense = {
                    "name": name,
                    "amount": amount,
                    "category": category
                }

                expenses.append(expense)
                save_data()
                print("Expense saved successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    # View all expenses
    elif choice == "3":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            total = 0

            print("\n=== YOUR EXPENSES ===")

            for expense in expenses:
                print(
                    expense["name"],
                    "- ₹", round(expense["amount"], 2),
                    "-", expense["category"]
                )
                total += expense["amount"]

            print("Total expenses: ₹", round(total, 2))

    # Show remaining budget
    elif choice == "4":
        total = sum(
            expense["amount"] for expense in expenses
        )

        remaining = budget - total

        print("Monthly budget: ₹", round(budget, 2))
        print("Total expenses: ₹", round(total, 2))
        print("Remaining budget: ₹", round(remaining, 2))

        if remaining < 0:
            print("Warning: You have exceeded your budget!")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    # Category-wise summary
    elif choice == "6":
        category_totals = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        if not category_totals:
            print("No expenses recorded yet.")
        else:
            print("\n=== CATEGORY SUMMARY ===")

            for category, total in category_totals.items():
                print(
                    category,
                    ": ₹",
                    round(total, 2)
                )

    else:
        print("Invalid choice! Enter a number from 1 to 6.")
