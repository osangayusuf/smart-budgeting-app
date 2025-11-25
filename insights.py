import pandas as pd
import streamlit as st
import plotly.express as px
import database as db


st.set_page_config(page_title="Smart Budgeting App - Insights", layout="wide")
st.markdown("# Insights")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        total_expenses = db.get_total_expenses()
        st.write(f"### Total Expenses: {total_expenses[0] if total_expenses[0] else 0}")
    with col2:
        average_expenses = db.get_average_expenses()
        st.write(
            f"### Average Expenses: {(average_expenses[0] if average_expenses[0] else 0):.2f}"
        )
    col3, col4 = st.columns(2)
    with col3:
        max_expense = db.get_max_expense()
        st.write(f"### Max Expense: {max_expense[0] if max_expense[0] else 0}")
    with col4:
        min_expense = db.get_min_expense()
        st.write(f"### Min Expense: {min_expense[0] if min_expense[0] else 0}")

st.markdown("---")

total_expenses_by_month = db.get_total_expenses_by_month()
monthly_df = pd.DataFrame(
    total_expenses_by_month,
    columns=[
        "year_month",
        "month_number",
        "year_number",
        "month_name",
        "amount",
    ],
).sort_values("year_month")

if monthly_df.empty:
    st.info("Add expenses to see monthly insights.")
else:
    available_months = ["All Months"] + monthly_df["year_month"].tolist()
    selected_month = st.selectbox("Filter by Month", available_months, index=0)

    st.markdown("### Monthly Expenses Bar Chart")
    if selected_month == "All Months":
        st.bar_chart(monthly_df, x="month_name", y="amount")
    else:
        filtered_monthly = monthly_df[monthly_df["year_month"] == selected_month]
        if not filtered_monthly.empty:
            st.bar_chart(filtered_monthly, x="month_name", y="amount")
        else:
            st.info(f"No expenses found for {selected_month}")

    st.markdown("### Expenses by Tag (Pie Chart)")
    year_month_filter = None if selected_month == "All Months" else selected_month
    expenses_by_tag = db.get_expenses_by_tag(year_month_filter)

    if expenses_by_tag:
        tag_df = pd.DataFrame(expenses_by_tag, columns=["tag", "amount"])
        fig = px.pie(
            tag_df,
            values="amount",
            names="tag",
            title=f"Expense Distribution by Tag{'' if selected_month == 'All Months' else f' ({selected_month})'}",
            hole=0.3,
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info(
            f"No tag data available{'' if selected_month == 'All Months' else f' for {selected_month}'}"
        )
