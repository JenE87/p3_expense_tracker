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
        print("2 - Exit")
        choice = input("> ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("No expense saved. See you next time.")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

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
            f"Date: {date_value}, Category: {category}, "
            "Description: {description or ""},"
            "Amount (in EUR): {amount}\n"
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


# Temporary manual test (TO BE DELETED LATER AND REPLACED BY A MAIN() FUNCTION)
# Add_expense()
main_menu()
