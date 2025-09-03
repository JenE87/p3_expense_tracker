import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Predefined categories
CATEGORIES = [
    "Food", "Transport", "Utilities", "Entertainment",
    "Insurance", "Medical", "Other"
    ]

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expense_tracker')


def prompt_date() -> str:
    """
    Ask for a date and validate format YYYY-MM-DD.
    """
    while True:
        value = input("Date (YYYY-MM-DD): ").strip()
        try:
            parsed = datetime.strptime(value, "%Y-%m-%d")
            if parsed.strftime("%Y-%m-%d") == value:
                return value
            else:
                print("Please use the strict format YYYY-MM-DD"
                      "(e.g. 2025-09-02).")
        except ValueError:
            print("Please enter a valid date in format YYYY-MM-DD.")


def prompt_category() -> str:
    """
    Ask for a category and validate against predefined list.
    Case-insensitive check.
    """
    while True:
        value = input(
                f"Category ({', '.join(CATEGORIES)}): "
                ).strip().capitalize()
        if value in CATEGORIES:
            return value
        print(f"Invalid category. Please choose from {', '.join(CATEGORIES)}")


def prompt_amount() -> float:
    """
    Ask for positive amount (accepts "," or ".").
    """
    while True:
        raw = input("Amount (in EUR): ").strip()
        # Allow European decimal comma
        raw = raw.replace(",", ".")
        try:
            amount = float(raw)
            if amount > 0:
                # Round to 2 decimals for consistency
                return round(amount, 2)
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number (e.g. 12,50).")


def main_menu():
    """
    Provide user with a short welcome and mini menu to choose next step.
    """
    while True:
        print("\nWelcome to the Expense Tracker")
        print("What would you like to do?\n")
        print("1 - Add an expense")
        print("2 - View totals")
        print("3 - Filter by category")
        print("4 - Filter by date")
        print("5 - View monthly totals")
        print("6 - Exit")
        choice = input("> ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_totals()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            filter_by_date()
        elif choice == "5":
            view_monthly_totals()
        elif choice == "6":
            print("Program closed successfully. See you next time.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, 5 or 6.")

        print("\n-----")


def add_expense():
    """
    Ask user for expense details and add them to the Google Sheet.
    Validate all inputs to prevent crashed or bad data.
    """
    print("\n--- Add a New Expense ---")

    print("Please provide the following information about your expense...\n")
    date_value = prompt_date()
    category = prompt_category()
    # Description is optional, but with trimmed blank spaces
    description = input("Description (optional): ").strip()
    amount = prompt_amount()

    # Check if user wants to proceed with input
    while True:
        confirm = input(
            f"\nSave this expense? [Y/N]\n"
            f"Date: {date_value}, "
            f"Category: {category}, "
            f"Description: {description or ""}, "
            f"Amount: {amount:.2f} EUR\n> "
        ).strip().lower()
        if confirm in ("y", "yes"):
            break
        if confirm in ("n", "no"):
            print("Cancelled. Expense not saved.")
            return
        print("Please answer with Y or N.")

    # Add expense to Google Sheet
    try:
        expenses_worksheet = SHEET.worksheet("expenses")
        expenses_worksheet.append_row(
            [date_value, category, description, amount],
            value_input_option="USER_ENTERED"
            )
        print("Expense added successfully!")
    except Exception as e:
        print("Could not save the expense. Please try again later.")
        print(e)


def view_totals():
    """
    Calculate and display the total of all expenses.
    """
    expenses_worksheet = SHEET.worksheet("expenses")
    data = expenses_worksheet.get_all_values()

    total = 0.0
    # Skip header
    for row in data[1:]:
        try:
            amount = float(row[3].replace(",", "."))
            total += amount
        except (ValueError, IndexError):
            continue

    print(f"\nTotal expenses: {total:.2f} EUR")


def filter_by_category():
    """
    Show all expenses for a chosen category.
    """
    category = prompt_category()
    expenses_worksheet = SHEET.worksheet("expenses")
    data = expenses_worksheet.get_all_values()

    filtered = [row for row in data[1:] if row[1].lower() == category.lower()]

    if not filtered:
        print(f"No expenses found in category '{category}'.")
    else:
        print(f"Expenses in category '{category}':")
        for row in filtered:
            print(*row, sep=", ")


def filter_by_date():
    """
    Show all expenses for a chosen date (YYYY-MM-DD).
    """
    date_value = prompt_date()
    expenses_worksheet = SHEET.worksheet("expenses")
    data = expenses_worksheet.get_all_values()

    filtered = [row for row in data[1:] if row[0] == date_value]

    if not filtered:
        print(f"No expenses found on {date_value}.")
    else:
        print(f"Expenses on {date_value}:")
        for row in filtered:
            print(*row, sep=", ", end=" EUR\n")


def view_monthly_totals():
    """
    Show total expenses grouped by year-month (YYYY-MM).
    """
    expenses_worksheet = SHEET.worksheet("expenses")
    data = expenses_worksheet.get_all_values()

    totals_by_month = {}

    for row in data[1:]:
        try:
            # Parse date as datetime object
            date_obj = datetime.strptime(row[0], "%Y-%m-%d")
            # Extract month
            month_key = date_obj.strftime("%Y-%m")
            # Grab values and transform them to a float
            amount = float(row[3].replace(",", "."))
            totals_by_month[month_key] = totals_by_month.get(
                month_key, 0) + amount

        except (ValueError, IndexError):
            continue

    print("\nMonthly totals:")
    for month, total in sorted(totals_by_month.items()):
        print(f"{month}: {total:.2f} EUR")


# Temporary manual test (TO BE DELETED LATER AND REPLACED BY A MAIN() FUNCTION)
main_menu()
