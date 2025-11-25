import streamlit as st
from datetime import date, timedelta

import database as db

st.set_page_config(page_title="Smart Budgeting App - View Expenses", layout="wide")
st.markdown("# View Expenses")

tags = db.get_tags()
tags_list = [tag[0] for tag in tags if tag[0]]

with st.expander("Filters", expanded=True):
    tag_selection = st.selectbox(
        "Tag",
        ["All"] + tags_list,
    )

    sort_options = {
        "Date": "date",
        "Amount": "amount",
        "Name": "name",
        "Tag": "tag",
        "ID": "id",
    }
    sort_by_label = st.selectbox(
        "Sort by",
        list(sort_options.keys()),
        index=0,
    )
    sort_direction_label = st.radio(
        "Sort order",
        ["Ascending", "Descending"],
        horizontal=True,
    )

    apply_date_filter = st.checkbox("Filter by date range")
    start_date = end_date = None
    if apply_date_filter:
        today = date.today()
        default_start = today - timedelta(days=30)
        col_start, col_end = st.columns(2)
        with col_start:
            start_date = st.date_input(
                "Start date",
                value=default_start,
                format="YYYY-MM-DD",
            )
        with col_end:
            end_date = st.date_input(
                "End date",
                value=today,
                format="YYYY-MM-DD",
            )

    apply_amount_filter = st.checkbox("Filter by amount range")
    min_amount = max_amount = None
    if apply_amount_filter:
        col_min, col_max = st.columns(2)
        with col_min:
            min_amount = st.number_input(
                "Minimum amount",
                min_value=0.0,
                value=0.0,
                step=1.0,
            )
        with col_max:
            max_amount = st.number_input(
                "Maximum amount",
                min_value=0.0,
                value=0.0,
                step=1.0,
            )

invalid_date_range = start_date and end_date and start_date > end_date
invalid_amount_range = (
    min_amount is not None and max_amount is not None and min_amount > max_amount
)

if invalid_date_range:
    st.error("Start date cannot be later than end date.")
if invalid_amount_range:
    st.error("Minimum amount cannot exceed maximum amount.")

if invalid_date_range or invalid_amount_range:
    expenses = []
else:
    expenses = db.get_expenses(
        tag=None if tag_selection == "All" else tag_selection,
        start_date=start_date.isoformat() if start_date else None,
        end_date=end_date.isoformat() if end_date else None,
        min_amount=min_amount if apply_amount_filter else None,
        max_amount=max_amount if apply_amount_filter else None,
        sort_by=sort_options[sort_by_label],
        sort_order="desc" if sort_direction_label == "Descending" else "asc",
    )

with st.container():
    if expenses:
        st.dataframe(expenses)
    else:
        st.info("No expenses found for the selected filters.")
