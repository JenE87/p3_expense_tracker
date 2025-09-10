# Expense Tracker 
A simple, reliable command-line Expense Tracker written in Python. It stores your entries in a connected Google Sheet, so your data stays transparent and portable. The app runs in the Code Institute mock terminal on Heroku and focuses on robust input validation and clean UX in the terminal.

[Here is the live Version of my project.](https://p3-expense-tracker-f310cbe43264.herokuapp.com/)
<img width="1373" height="625" alt="Screenshot 2025-09-03 at 20 14 40" src="https://github.com/user-attachments/assets/6847ccf8-fd52-4d0c-a957-f68ea3bf4b73" />

## Project Overview
The Expense Tracker is a simple command-lin app to record daily expenses directly into a Google Sheet.
It is useful for:
- Individuals who want to keep track of their personal budget
- Families who want shared visibility of their spending
- Small groups (e.g. roommates, friends, colleagues) who split costs and need an easy record

The focus is on simplicity, strict input validation, and reliable data storage.
<img width="753" height="466" alt="Screenshot 2025-09-05 134803" src="https://github.com/user-attachments/assets/8b200302-538a-4ae6-8b10-bda41ac74541" />

## Features
### Existing Features
- Add new expenses with strict input Validation
<img width="735" height="394" alt="Screenshot 2025-09-05 141003" src="https://github.com/user-attachments/assets/102dbb8c-2028-4a54-89bb-66e64d4cad69" />


- Data is stored in Google Sheets via API
<img width="733" height="357" alt="Screenshot 2025-09-05 141030" src="https://github.com/user-attachments/assets/bdf0a98b-0329-452a-af23-ff456db8a1d2" />


- View total expenses
<img width="748" height="297" alt="image" src="https://github.com/user-attachments/assets/7e6472cd-6f2c-467f-a1ce-8f4345f5e709" />


- Filter by name
<img width="733" height="331" alt="image" src="https://github.com/user-attachments/assets/b0002aea-9c1e-4102-8ee0-1c03b1d654d4" />


- Filter by category
<img width="738" height="246" alt="image" src="https://github.com/user-attachments/assets/d3f7b0e8-ad07-42be-aebd-cd4fdac8a4ed" />


- Filter by date
<img width="732" height="285" alt="image" src="https://github.com/user-attachments/assets/da6595ec-9b5f-40eb-8aa3-7095d1976b35" />


- View monthly totals
<img width="740" height="180" alt="image" src="https://github.com/user-attachments/assets/29490d11-dbc6-42a7-a63b-2eca2d8a3427" />


## Future Features (optional)
- Add categories
- Add totals by name and/or categories
- Add Budget Goals
- Visualize spending with charts
- Export to CSV

## Technologies Used
- Python 3
- gspread (Google Sheets API)
- Google OAuth2 Credentials
- Heroku (deployment)

## Google Sheet Setup
- Create a Google Sheet with a tab named `expenses`
- Columns
	- Date (YYYY-MM-DD)
  	- Name
  	- Amount (in EUR)
	- Category
	- Description
<img width="744" height="435" alt="image" src="https://github.com/user-attachments/assets/eab6c78a-96c3-4fa0-87ed-2ebeec4d38fa" />


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
| Filter by Name                    | Enter `Jenny`                  | Only rows of Jenny displayed  | Pass      |
|                                   | Enter `Bob` (no data)          | Message displayed: no data found for NAME | Pass      |
| Filter by Category                | Enter `Food`                   | Only rows with Food expenses displayed    | Pass      |
|                                   | Enter `invalid`                | Rejected, prompt again for valid input    | Pass      |
| Filter by Date                    | Enter `2025-09-02`             | Expenses only from this date displayed    | Pass      |
|                                   | Enter `2025-02-02` (no data)   | Message displayed: no data found for DATE |  Pass     |
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
<img width="974" height="640" alt="Screenshot 2025-09-05 133240" src="https://github.com/user-attachments/assets/0b94e463-48a9-4b54-a190-d48c9167cf2c" />

### Fixed Bugs
- **Category Input Validation**: Initially, the input was normalized using `.capitalize()`. This meant both food and Food were accepted, but variations like `fOOD` were rejected. The fix was to switch to `.lower()` comparison, ensuring the validation is now fully case-insensitive and consistent.
- **Heroku Deployment Error (Procfile & .gitignore)**: Incorrect adjustments in the `Procfile` and `.gitignore` caused Heroku deployment to fail. Resetting both files to the original template Setup fixed the issue.
- **Python Version Mismatch**: Deployment failed because the `.python-version` file specified `3.12.2`. Heroku only accepts major versions, so this was corrected to `3.12`, resolving the bug.
- **Amount Validation Rounding**: Initially, inputs like `12.468` were stored as-is, leading to inconsistent decimals. The fix was to round all amounts to 2 decimal places, ensuring consistent formatting.
- **Blank Description Handling**: Empty description input caused unwanted whitespace in the Google Sheet. The fix was to apply `.strip()` and allow and empty string if no description was entered.
- **Case Handling for Names**: Initially names were stores with `.capitalize()`, which led to inconsistency (e.g. MAX -> Max). Validation and filtering were improved to use case-insensitive checks while storing the raw input.

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
- [Real Python](https://realpython.com/)


