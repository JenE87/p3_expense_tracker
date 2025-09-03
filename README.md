# Expense Tracker 
A command-line Expense Tracker written in Python that stores and manages expenses using a connected Google Sheet. The Tracker run in the Code Institute mock terminal on Heroku.

SHORT INTRO TO BE ADDED

Here is the live Version of the Expense Tracker. LINKLINKLINK

## Project Overview
WHAT DOES THE TRACKER DO 
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
| Filter by Category                | Enter `Food`                   | Only rows with Food expenses displayed |           |
|                                   | Enter `invalid`                | Show invalid input, prompt again       |           |
| Filter by Date                    | Enter `2025-09-02`             | Expenses only from this date displayed |           |
|                                   | Enter `2025-02-02` (no data)   | Message displayed that no data found for DATE      |         |
| View Monthly Totals               | (adding totals automatically)  | Groups totals per month correctly      |           |
| Menu Navigation                   | `1` (Add an expense)           | Add Expense feature initiates with prompt for DATE |         |
|                                   | `2` (View Totals)              | Total expenses displayed               |           |
|                                   | `3` (Filter by category)       | Category prompt displayed              |           |
|                                   | `4` (Filter by date)           | Date prompt (YYYY-MM-DD) displayed     |           |
|                                   | `5` (View Monthly totals)      | Groups totals per month correctly      |           |
|                                   | `6` (Exit)                     | Program Ends. Exit message displayed   |           |
|                                   | `9` (invalid option)           | Rejected, prompt again                 |           |


### PEP8 Python Validator 
Passed the code through a PEP8 linter and confirmed there are no problems.

### Fixed Bugs
- 

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

--------------------------------

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 26, 2025**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
