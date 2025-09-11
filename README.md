# Expense Tracker 
A simple, reliable command-line Expense Tracker written in Python. It stores your entries in a connected Google Sheet, so your data stays transparent and portable. The app runs in the Code Institute mock terminal on Heroku and focuses on robust input validation and clean UX in the terminal.

[Here is the live Version of my project.](https://p3-expense-tracker-f310cbe43264.herokuapp.com/)

<img width="1373" height="625" alt="Screenshot 2025-09-03 at 20 14 40" src="https://github.com/user-attachments/assets/6847ccf8-fd52-4d0c-a957-f68ea3bf4b73" />

## Project Overview
The Expense Tracker is a simple command-line app to record daily expenses directly into a Google Sheet.
It is useful for:
- Individuals who want to keep track of their personal budget
- Families who want shared visibility of their spending
- Small groups (e.g. roommates, friends, colleagues) who split costs and need an easy record

The focus is on simplicity, strict input validation, and reliable data storage.
<img width="753" height="466" alt="Screenshot 2025-09-05 134803" src="https://github.com/user-attachments/assets/8b200302-538a-4ae6-8b10-bda41ac74541" />

## Features
### Existing Features
- Add new expenses with strict input Validation
<img width="736" height="402" alt="Screenshot 2025-09-10 140831" src="https://github.com/user-attachments/assets/6b238378-f7d4-46a6-8a66-3ff43463b3bf" />

- Data is stored in Google Sheets via API
<img width="756" height="500" alt="Screenshot 2025-09-10 140946" src="https://github.com/user-attachments/assets/2af624c3-f2e2-4804-be7d-f9238a6a631e" />

- View total expenses
<img width="748" height="297" alt="image" src="https://github.com/user-attachments/assets/7e6472cd-6f2c-467f-a1ce-8f4345f5e709" />

- Filter by name
<img width="736" height="313" alt="Screenshot 2025-09-10 141057" src="https://github.com/user-attachments/assets/843234d5-21d6-41ad-ba3f-d3bc7509275a" />

- Filter by category
<img width="742" height="346" alt="Screenshot 2025-09-10 141542" src="https://github.com/user-attachments/assets/fc488baa-0877-406b-b415-83cfcd9d8e1e" />

- Filter by date
<img width="741" height="226" alt="Screenshot 2025-09-10 141637" src="https://github.com/user-attachments/assets/df7f84f7-bab4-441a-8084-01a18dedb1ff" />

- View monthly totals
<img width="740" height="180" alt="image" src="https://github.com/user-attachments/assets/29490d11-dbc6-42a7-a63b-2eca2d8a3427" />

## Future Features (optional)
- Add categories
- Add totals by name and/or categories
- Add Budget Goals
- Visualize spending with charts
- Export to CSV

## Technologies Used
The following tools and technologies were used to build this project:
### Languages
- **Python 3.12** - main programming language

### Libraries & Dependencies
- **gspread** - for interacting with Google Sheets
- **google-auth** - for authentication with Google APIs
- **datetime** - for handling and validating dates

### Tools & Services
- **Git** & **GitHub** - version control and repository hosting
- **Heroku** - deployment platform (with Python & NodeJS buildpacks)
- **Google Sheets API** - database layer for expense storage
- **Google Drive API** - enables sheet access and sharing
- **LanguageTool** - for grammar, spelling, paraphrasing support in code strings and documentation
- **ChatGPT** - for planning, debugging, and documentation support
- **requirements.txt** - for dependency management

### Development & IDE
- **VS Code** - code editor
- **Python virtual environment (venv)** - to isolate dependencies locally

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
<img width="959" height="641" alt="Screenshot 2025-09-10 191501" src="https://github.com/user-attachments/assets/e5599560-2bbc-4921-9cc6-4aaef7601410" />

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
### Local Setup
To run this project locally on your machine:
1. Clone the repository of this project or the [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) provided by Code Institute's LMS.
2. Create and activate a virtual environment using venv and Python version 3.12.8
3. Install dependencies by selecting ok during set up of the virtual environment or using `pip install -r requirements.txt`
   	(*Note: If you add new dependencies locally, update the `requirements.txt` file using `pip3 freeze > requirements.txt` before pushing to GitHub.*)
4. Check that your venv is running. If not, activate the virtual environment, using for example:
 	- `source .venv/bin/activate` (*for Mac/Linux*)
	- `venv\Scripts\activate` OR `.\.venv\Scripts\Activate.ps1`(*for Windows*)
5. Add `.venv` to the `.gitignore` file to ensure the virtual environemnt folder is excluded from version control.
6. Google Sheet Setup
   - Create a Google Cloud project and enable the **Google Sheets API** and **Google Drive API**.
   - Generate service account credentials and download the `creds.json` file.
   - Place `creds.json` in root directory of your project (Do not commit this file; it should be in `.gitignore`).
   - You will need to share your Google Sheet with the **client_email** from your `creds.json` file so the app has permission to read and write to it.
   - Create a Google Sheet named `expense_tracker` with a tab called `expenses` and the following columns:
     	- Date
     	- Name
     	- Amount (in EUR)
     	- Category
     	- Description
7. Run the program locally with `python3 run.py`

### Version Control
This project uses **Git** for version control.

### Heroku Deployment
1. Make sure your repository includes:
	- `requirements.txt` (lists Python dependencies)
	- `Procfile` (defines how Heroku runs your app `web: node index.js`)
	- `.gitignore` (excludes files like `creds.json`)
2. Log into [Heroku](https://www.heroku.com/) and create a **new app**.
3. Under **Settings** create config vars, by adding the following keys and values:
	- KEY: `CREDS` and VALUE: paste the entire content of your `creds.json` file here
	(*Note: Never push your `creds.json` file directly to GitHub. It is already in `.gitignore`. Using Config Vars keeps your credentials secure.*)
	- KEY: `PORT` and VALUE: `8000`
4. Under **Settings**, add the buildpacks in this order:
	- `Python`
	- `NodeJS` 
5. Connect your Heroku app to your **GitHub repository**:
	- in the **Deploy** tab, link to your GitHub account and repository.
	- Enable **Automatic Deploys** so your app updates every time you push changes to GitHub.
6. Commit and push your changes (command i.e. "Prepare for Heroku deployment")
7. If needed, trigger a manual build in Heroku by clicking **Deploy Branch** under the **Deploy** tab
8. Once the build is finished, click **Open App** to launch your Expense Tracker

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
- [Genepy](https://genepy.org/)


