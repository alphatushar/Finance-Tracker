import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# File to store expenses
FILE_NAME = "expenses.csv"

# Initialize file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
    df.to_csv(FILE_NAME, index=False)


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")

    new_entry = pd.DataFrame([[date, category, amount, note]],
                             columns=["Date", "Category", "Amount", "Note"])

    new_entry.to_csv(FILE_NAME, mode="a", header=False, index=False)
    print("✅ Expense added successfully!")


def view_summary():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses recorded yet.")
        return

    print("\n--- Expense Summary ---")
    print(df.groupby("Category")["Amount"].sum())
    print("\nTotal Spent:", df["Amount"].sum())


def visualize_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No data to visualize.")
        return

    df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.show()


def main():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Visualize Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            visualize_expenses()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()