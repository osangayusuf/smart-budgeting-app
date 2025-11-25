import streamlit as st
import database as db
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Smart Budgeting App - Home", layout="wide", page_icon="💰"
)

st.title("💰 Smart Budgeting App")
st.markdown("### Welcome to Your Personal Finance Manager")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_expenses = db.get_total_expenses()
    total = total_expenses[0] if total_expenses[0] else 0
    st.metric(label="💵 Total Expenses", value=f"₦{total:,.2f}", delta=None)

with col2:
    average_expenses = db.get_average_expenses()
    avg = average_expenses[0] if average_expenses[0] else 0
    st.metric(label="📊 Average Expense", value=f"₦{avg:,.2f}", delta=None)

with col3:
    max_expense = db.get_max_expense()
    max_val = max_expense[0] if max_expense[0] else 0
    st.metric(label="📈 Highest Expense", value=f"₦{max_val:,.2f}", delta=None)

with col4:
    expenses = db.get_expenses()
    expense_count = len(expenses)
    st.metric(label="🧾 Total Transactions", value=expense_count, delta=None)

st.markdown("---")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("### 📅 Recent Activity")

    recent_expenses = db.get_expenses(sort_by="date", sort_order="desc")

    if recent_expenses:
        recent_df = pd.DataFrame(
            recent_expenses[:5], columns=["ID", "Name", "Amount", "Date", "Tag"]
        )
        recent_df["Amount"] = recent_df["Amount"].apply(lambda x: f"₦{x:,.2f}")
        recent_df = recent_df.drop(columns=["ID"])

        st.dataframe(recent_df, use_container_width=True, hide_index=True)

        if len(recent_expenses) > 5:
            st.info(
                f"Showing 5 of {len(recent_expenses)} transactions. View all in the 'View Expenses' page."
            )
    else:
        st.info("No expenses recorded yet. Get started by adding your first expense!")

with col_right:
    st.markdown("### 🏷️ Top Categories")

    expenses_by_tag = db.get_expenses_by_tag()

    if expenses_by_tag:
        tag_df = pd.DataFrame(expenses_by_tag[:5], columns=["Category", "Total"])

        for idx, row in tag_df.iterrows():
            st.markdown(f"**{row['Category']}**: ₦{row['Total']:,.2f}")
    else:
        st.info("No categories yet. Start tracking expenses by category!")

st.markdown("---")

st.markdown("### 📊 Spending Trend (Last 30 Days)")

thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
recent_expenses_data = db.get_expenses(
    start_date=thirty_days_ago, sort_by="date", sort_order="asc"
)

if recent_expenses_data:
    trend_df = pd.DataFrame(
        recent_expenses_data, columns=["ID", "Name", "Amount", "Date", "Tag"]
    )
    trend_df["Date"] = pd.to_datetime(trend_df["Date"])
    daily_spending = trend_df.groupby("Date")["Amount"].sum().reset_index()

    fig = px.line(
        daily_spending,
        x="Date",
        y="Amount",
        title="Daily Spending Over Last 30 Days",
        labels={"Amount": "Amount (₦)", "Date": "Date"},
    )
    fig.update_traces(line_color="#1f77b4", line_width=2)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No expenses in the last 30 days. Add expenses to see your spending trend!")

st.markdown("---")

st.markdown("### 🚀 Quick Actions")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.page_link("add_expenses.py", label="💸 Add New Expense", icon="➕")

with col_b:
    st.page_link("view_expenses.py", label="📊 View All Expenses", icon="👁️")

with col_c:
    st.page_link("insights.py", label="📈 View Insights", icon="🔍")

st.markdown("---")
st.markdown(
    "##### 💡 Tip: Keep track of your daily expenses to better understand your spending habits!"
)
