# Expense Tracker 
A simple, reliable command-line Expense Tracker written in Python. It stores your entries in a connected Google Sheet, so your data stays transparent and portable. The app runs in the Code Institute mock terminal on Heroku and focuses on robust input validation and clean UX in the terminal.

[Here is the live Version of my project.](https://p3-expense-tracker-f310cbe43264.herokuapp.com/)

## Project Overview
**STILL TO BE INCLUDED** WHAT DOES THE TRACKER DO & 
FOR WHO IS THE TRACKER USEFUL

## Features
### Existing Features
- Add new expenses with strict input Validation
- Data is stored in Google Sheets via API
- View total expenses
- Filter by category
- Filter by date
- View monthly totals

## Future Features (optional)
- Export to CSV
- Visualize spending with charts
- Add Budget Goals

## Technologies Used
- Python 3
- gspread (Google Sheets API)
- Google OAuth2 Credentials
- Heroku (deployment)


## Google Sheet Setup
- Create a Google Sheet with a tab named `expenses`
- Columns
	- Date (YYYY-MM-DD)
	- Category
	- Description
	- Amount (in EUR)


## Testing
### Manual Testing
| Feature                           | Test Input                     | Expected Result               | Pass/Fail |
|-----------------------------------|--------------------------------|-------------------------------|-----------|
| Add Expense - Date validation     | `2025-09-02`                   | Accepted, saved correctly     | Pass      |
|                                   | `02-09-2025`                   | Rejected, prompt again        | Pass      |
|                                   | `2025-9-2`                     | Rejected, prompt again        | Pass      |
|                                   | `abcd`                         | Rejected, prompt again        | Pass      |
| Add Expense - Category Validation | `Food`                         | Accepted                      | Pass      |
|                                   | `food`                         | Accepted (case-insensitive)   | Pass      |
|                                   | `fOOD`                         | Accepted (case-insensitive)   | Pass      |
|                                   | `invalid`                      | Rejected, prompt again        | Pass      |
| Add Expense - Description         | (empty Input)                  | Saved as blank                | Pass      |
|                                   | `Teamlunch`                    | Saved correctly               | Pass      |
| Add Expense - Amount Validation   | `12.50`                        | Accepted as `12.50`           | Pass      |
|                                   | `12,50`                        | Accepted as `12.50`           | Pass      |
|                                   | `1.879`                        | Accepted as `1.88`            | Pass      |
|                                   | `-5`                           | Rejected, prompt again        | Pass      |
|                                   | `abc`                          | Rejected, prompt again        | Pass      |
| Confirmation Prompt               | Input `Y`                      | Expense saved to Google Sheet | Pass      |
|                                   | Input `N`                      | Expense cancelled             | Pass      |
| View Totals	                    | (after adding known values)    | Shows correct total expenses  | Pass      |
| Filter by Category                | Enter `Food`                   | Only rows with Food expenses displayed | Pass      |
|                                   | Enter `invalid`                | Rejected, prompt again        | Pass      |
| Filter by Date                    | Enter `2025-09-02`             | Expenses only from this date displayed | Pass      |
|                                   | Enter `2025-02-02` (no data)   | Message displayed that no data found for DATE      |  Pass   |
| View Monthly Totals               | (adding totals automatically)  | Groups totals per month correctly      | Pass      |
| Menu Navigation                   | `1` (Add an expense)           | Add Expense feature initiates with prompt for DATE | Pass    |
|                                   | `2` (View Totals)              | Total expenses displayed               | Pass      |
|                                   | `3` (Filter by category)       | Category prompt displayed              | Pass      |
|                                   | `4` (Filter by date)           | Date prompt (YYYY-MM-DD) displayed     | Pass      |
|                                   | `5` (View Monthly totals)      | Groups totals per month correctly      | Pass      |
|                                   | `6` (Exit)                     | Program Ends. Exit message displayed   | Pass      |
|                                   | `9` (invalid option)           | Rejected, prompt again                 | Pass      |


### PEP8 Python Validator 
Passed the code through a PEP8 linter and confirmed there are no problems.

### Fixed Bugs
- **Category Input Validation**: Initially, the input was normalized using .capitalize(). This meant both food and Food were accepted, but variations like fOOD were rejected. The fix was to switch to .lower() comparison, ensuring the validation is now fully case-insensitive and consistent.
- **Heroku Deployment Error (Procfile & .gitignore)**: Incorrect adjustments in the `Procfile` and `.gitignore` caused Heroku deployment to fail. Resetting both files to the original template Setup fixed the issue.
- **Python Version Mismatch**: Deployment failed because the `.python-version` file specified `3.12.2`. Heroku only accepts major versions, so this was corrected to `3.12`, resolving the bug.

### Unfixed Bugs
None

## Deployment
This Project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
	- Fork or clone this repository
	- Create a new Heroku app
	- Set the buildpacks to `Python` and `NodeJS` in that order
	- Link the Heroku app to the repository
	- Click on **Deploy**

## Credits
### Code
All code is inspired by lessons and modules included in the Code Institute's Full Stack Software Development Common Curriculum in the Learning Management System.

Other learning resources:
- [Python.org](https://www.python.org/)
- [W3 schools](https://www.w3schools.com/)
- [Geeksforgeeks - Python](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)
- [Stack Overflow](https://stackoverflow.com/questions)
- [Codeacademy Forums](https://discuss.codecademy.com/c/faqs/python-faq/1793)


