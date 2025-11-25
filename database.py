import sqlite3

DATABASE_NAME = "expenses.db"


def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            tag TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn, cursor


def get_expenses(
    tag=None,
    start_date=None,
    end_date=None,
    min_amount=None,
    max_amount=None,
    sort_by="date",
    sort_order="asc",
):
    conn, cursor = init_db()
    query = "SELECT * FROM expenses"
    params = []
    conditions = []

    if tag:
        conditions.append("tag = ?")
        params.append(tag)
    if start_date:
        conditions.append("date >= ?")
        params.append(start_date)
    if end_date:
        conditions.append("date <= ?")
        params.append(end_date)
    if min_amount is not None:
        conditions.append("amount >= ?")
        params.append(min_amount)
    if max_amount is not None:
        conditions.append("amount <= ?")
        params.append(max_amount)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    valid_sort_columns = {"id", "name", "amount", "date", "tag"}
    sort_column = sort_by if sort_by in valid_sort_columns else "date"
    sort_direction = "desc" if sort_order and sort_order.lower() == "desc" else "asc"
    query += f" ORDER BY {sort_column} {sort_direction}"

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results


def get_tags():
    conn, cursor = init_db()
    cursor.execute("SELECT DISTINCT tag FROM expenses")
    return cursor.fetchall()


def add_expense(name, amount, date, tag):
    conn, cursor = init_db()
    cursor.execute(
        "INSERT INTO expenses (name, amount, date, tag) VALUES (?, ?, ?, ?)",
        (name, amount, date, tag),
    )
    conn.commit()


def get_total_expenses():
    conn, cursor = init_db()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    return cursor.fetchone()


def get_average_expenses():
    conn, cursor = init_db()
    cursor.execute("SELECT AVG(amount) FROM expenses")
    return cursor.fetchone()


def get_max_expense():
    conn, cursor = init_db()
    cursor.execute("SELECT MAX(amount) FROM expenses")
    return cursor.fetchone()


def get_min_expense():
    conn, cursor = init_db()
    cursor.execute("SELECT MIN(amount) FROM expenses")
    return cursor.fetchone()


def get_total_expenses_by_month():
    conn, cursor = init_db()
    cursor.execute("""
        SELECT 
            strftime('%Y-%m', date) as year_month, 
            strftime('%m', date) as month_number,
            strftime('%Y', date) as year_number,
            CASE 
                WHEN strftime('%m', date) = '01' THEN 'January'
                WHEN strftime('%m', date) = '02' THEN 'February'
                WHEN strftime('%m', date) = '03' THEN 'March'
                WHEN strftime('%m', date) = '04' THEN 'April'
                WHEN strftime('%m', date) = '05' THEN 'May'
                WHEN strftime('%m', date) = '06' THEN 'June'
                WHEN strftime('%m', date) = '07' THEN 'July'
                WHEN strftime('%m', date) = '08' THEN 'August'
                WHEN strftime('%m', date) = '09' THEN 'September'
                WHEN strftime('%m', date) = '10' THEN 'October'
                WHEN strftime('%m', date) = '11' THEN 'November'
                WHEN strftime('%m', date) = '12' THEN 'December'
            END as month_name,
            SUM(amount) 
        FROM expenses 
        GROUP BY year_month
        ORDER BY year_month
    """)
    return cursor.fetchall()


def get_expenses_by_tag(year_month=None):
    conn, cursor = init_db()
    if year_month:
        cursor.execute(
            """
            SELECT tag, SUM(amount) as total
            FROM expenses
            WHERE strftime('%Y-%m', date) = ?
            GROUP BY tag
            ORDER BY total DESC
        """,
            (year_month,),
        )
    else:
        cursor.execute("""
            SELECT tag, SUM(amount) as total
            FROM expenses
            GROUP BY tag
            ORDER BY total DESC
        """)
    return cursor.fetchall()
