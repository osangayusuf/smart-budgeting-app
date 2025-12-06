import streamlit as st

def main():
    # Define the pages
    home = st.Page("home.py", title="Home", icon="🏠", default=True)
    add_expenses = st.Page("add_expenses.py", title="Add Expenses", icon="💸")
    view_expenses = st.Page("view_expenses.py", title="View Expenses", icon="📊")
    insights = st.Page("insights.py", title="Insights", icon="📈")

    # Set up navigation
    pg = st.navigation([home, add_expenses, view_expenses, insights])

    # Run the selected page
    pg.run()

if __name__ == "__main__":
    main()