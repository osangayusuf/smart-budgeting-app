import streamlit as st
import database as db

st.set_page_config(
            page_title="Smart Budgeting App - Add Expenses", layout="wide"
        )
st.markdown("# Add Expenses")
with st.container():
    with st.form(key="add_expense_form"):
        expense_name = st.text_input(
            "Expense Name", placeholder="Enter expense name"
        )
        expense_name
        expense_amount = st.number_input("Expense Amount", min_value=0.0)
        expense_amount
        expense_date = st.date_input("Expense Date")
        expense_date
        expense_tag = st.text_input(
            "Expense Tag", placeholder="Enter expense tag"
        )
        expense_tag
        submit_button = st.form_submit_button("Add Expense")

if submit_button:
    if (
        not expense_name
        or not expense_amount
        or not expense_date
        or not expense_tag
    ):
        st.warning("Please fill all the fields.")
    else:
        try:
            db.add_expense(expense_name, expense_amount, expense_date, expense_tag)
            st.success("Expense added successfully!")
        except Exception as e:
            st.error(f"Error adding expense: {str(e)}")