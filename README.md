# 💰 Smart Budgeting App

A personal finance management application built with Streamlit that helps you track expenses, visualize spending patterns, and gain insights into your financial habits.

## 📋 Description

Smart Budgeting App is an intuitive web-based expense tracker that allows you to manage your personal finances effectively. The application provides a clean interface to add, view, and analyze your expenses with interactive visualizations and comprehensive filtering options.

### Key Features

- **📊 Dashboard Overview**: View key metrics including total expenses, average spending, highest expense, and transaction count
- **💸 Expense Tracking**: Add and categorize expenses with custom tags
- **📈 Visual Analytics**: Interactive charts and graphs showing spending trends over time
- **🏷️ Category Management**: Track expenses by categories and see top spending categories
- **🔍 Advanced Filtering**: Filter expenses by date range, amount, category, and more
- **📅 Time-based Analysis**: View spending trends by day, month, or custom periods
- **💡 Insights**: Get detailed breakdowns of your spending patterns and monthly comparisons

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Database**: SQLite
- **Data Processing**: Pandas
- **Visualizations**: Plotly, Matplotlib
- **Language**: Python 3.x

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

### Step 1: Clone or Download the Repository

If you have the project in a repository:

```bash
git clone <your-repository-url>
cd smart-budgeting-app
```

Or navigate to your project directory if you already have the files locally.

### Step 2: Set Up a Virtual Environment

Using a virtual environment is recommended to keep dependencies isolated.

#### On Windows:

**Using Command Prompt:**

```cmd
python -m venv venv
venv\Scripts\activate
```

**Using PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

_Note: If you encounter an execution policy error in PowerShell, run:_

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Once your virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies including Streamlit, Pandas, Plotly, and other required libraries.

### Step 4: Verify Installation

You can verify that all packages are installed correctly by running:

```bash
pip list
```

## 🎯 Running the Application

1. Make sure your virtual environment is activated (you should see `(venv)` in your terminal prompt)

2. Run the Streamlit application:

```bash
streamlit run app.py
```

3. The application will automatically open in your default web browser at `http://localhost:8501`

4. If it doesn't open automatically, navigate to the URL shown in your terminal (typically `http://localhost:8501`)

## 📁 Project Structure

```
smart-budgeting-app/
├── app.py                 # Main application entry point
├── home.py               # Home page with dashboard overview
├── add_expenses.py       # Page for adding new expenses
├── view_expenses.py      # Page for viewing and filtering expenses
├── insights.py           # Page for detailed analytics and insights
├── database.py           # Database operations and queries
├── requirements.txt      # Project dependencies
├── expenses.db          # SQLite database (created automatically)
└── README.md            # Project documentation
```

## 💡 Usage Guide

### Adding Expenses

1. Navigate to the **"Add Expenses"** page using the sidebar
2. Fill in the expense details:
   - Name/Description of the expense
   - Amount (in your currency)
   - Date of the transaction
   - Category/Tag
3. Click "Add Expense" to save

### Viewing Expenses

1. Go to the **"View Expenses"** page
2. Use filters to narrow down expenses by:
   - Date range
   - Amount range
   - Category
3. Sort expenses by different columns
4. View expenses in a detailed table format

### Analyzing Insights

1. Visit the **"Insights"** page to see:
   - Monthly spending trends
   - Category-wise breakdown
   - Spending patterns over time
   - Comparative analytics

### Dashboard

The **Home** page provides a quick overview of:

- Total expenses
- Average expense per transaction
- Highest single expense
- Recent transactions
- Top spending categories
- 30-day spending trend

## 🔧 Troubleshooting

### Virtual Environment Issues

**Problem**: Virtual environment won't activate on Windows PowerShell

- **Solution**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Problem**: `python` command not found

- **Solution**: Try using `python3` instead, or ensure Python is added to your PATH

### Application Issues

**Problem**: Streamlit command not found

- **Solution**: Ensure virtual environment is activated and dependencies are installed

**Problem**: Database errors

- **Solution**: Delete `expenses.db` file and restart the application (it will create a fresh database)

## 🔄 Deactivating the Virtual Environment

When you're done working with the application, you can deactivate the virtual environment:

```bash
deactivate
```

## 📝 Notes

- The application uses SQLite as the database, which is stored locally in `expenses.db`
- All data is stored locally on your machine
- The currency symbol (₦) can be customized in the source code if needed
- The application automatically creates the database on first run

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available for personal and educational use.

## 📧 Contact

For questions or suggestions, please reach out to the project maintainer.

---

**Happy Budgeting! 💰📊**
