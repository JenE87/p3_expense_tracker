import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expense_tracker')

#Helper Functions for Validation of inputs
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
                print("Please use the strict format YYYY-MM-DD (e.g. 2025-09-02).")
        except ValueError:
            print("Please enter a valid date in format YYYY-MM-DD.")

def prompt_non_empty(label: str) -> str:
    """
    Ask for a non-empty string and trim extra spaces.
    """
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print("This field cannot be empty.")

def prompt_amount() -> float:
    """
    Ask for positive amount (accepts "," or ".").
    """
    while True:
        raw = input("Amount (in EUR): ").strip()
        raw = raw.replace(",", ".") #allow European decimal comma
        try:
            amount = float(raw)
            if amount > 0:
                return round(amount, 2) #round to 2 decimals for consistency
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number (e.g. 12,50).")

def add_expense():
    """
    Ask user for expense details and add them to the Google Sheet.
    """
    print("\n---Add a New Expense---\n")


#Temporary manual test (TO BE DELETED LATER AND REPLACED BY A MAIN() FUNCTION)
#add_expense()
prompt_amount()
