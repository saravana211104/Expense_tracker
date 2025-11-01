import mysql.connector
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#Database Connection with Error Handling
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="expense_db"
    )
    cursor = conn.cursor()
except mysql.connector.Error as e:
    print("Database Connection Error:", e)
    exit()


#Input Validation Functions
def get_valid_date(prompt):
    while True:
        date = input(prompt)
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid Date Format! Please use YYYY-MM-DD.")


def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Amount! Enter a number.")


def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid ID! Must be a number.")


#CRUD Functions
def add_expense():
    date = get_valid_date("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = get_valid_float("Enter amount: ")
    description = input("Enter description: ")
    payment_mode = input("Enter payment mode: ")
    merchant_name = input("Enter merchant name: ")
    location = input("Enter location: ")
    notes = input("Enter notes: ")
    created_by = input("Enter your name: ")

    query = """
    INSERT INTO expenses(date, category, amount, description, payment_mode,
    merchant_name, location, notes, created_by)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    values = (date, category, amount, description, payment_mode,
              merchant_name, location, notes, created_by)
    try:
        cursor.execute(query, values)
        conn.commit()
        print("Expense Added Successfully!")
    except Exception as e:
        print("Error:", e)


def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    result = cursor.fetchall()
    if not result:
        print("No expenses found!")
    for row in result:
        print(row)


def update_expense():
    expense_id = get_valid_int("Enter expense ID to update: ")
    new_amount = get_valid_float("Enter new amount: ")

    cursor.execute("UPDATE expenses SET amount=%s WHERE expense_id=%s",
                   (new_amount, expense_id))
    conn.commit()
    print("Expense Updated!")


def delete_expense():
    expense_id = get_valid_int("Enter expense ID to delete: ")

    cursor.execute("DELETE FROM expenses WHERE expense_id=%s",
                   (expense_id,))
    conn.commit()
    print("Expense Deleted!")


def export_to_excel():
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    if not data:
        print("No data to export!")
        return

    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(data, columns=columns)
    df.to_excel("expense_report.xlsx", index=False)
    print("Excel Report Generated: expense_report.xlsx")


# Summary / Analytics Feature
def summary_report():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    total = total if total else 0

    print("\n Expense Summary:")
    print(f" Total Expense: ₹{total:.2f}")

    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    result = cursor.fetchall()
    if result:
        print("\nCategory Wise Expense:")
        for category, amt in result:
            print(f"- {category}: ₹{amt:.2f}")

def search_by_date():
    date = get_valid_date("Enter date (YYYY-MM-DD) to search: ")
    cursor.execute("SELECT * FROM expenses WHERE date=%s", (date,))
    result = cursor.fetchall()

    if not result:
        print(" No expenses found on this date.")
    else:
        for row in result:
            print(row)


def search_by_category():
    category = input("Enter category name: ")
    cursor.execute("SELECT * FROM expenses WHERE category LIKE %s", (f"%{category}%",))
    result = cursor.fetchall()

    if not result:
        print(" No expenses found in this category.")
    else:
        for row in result:
            print(row)


def search_by_date_range():
    print("Enter date range:")
    start_date = get_valid_date("From (YYYY-MM-DD): ")
    end_date = get_valid_date("To (YYYY-MM-DD): ")

    cursor.execute(
        "SELECT * FROM expenses WHERE date BETWEEN %s AND %s ORDER BY date ASC",
        (start_date, end_date)
    )
    result = cursor.fetchall()

    if not result:
        print(" No expenses found in this range.")
    else:
        for row in result:
            print(row)

def category_chart():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    result = cursor.fetchall()

    if not result:
        print(" No data to plot!")
        return

    categories = [row[0] for row in result]
    totals = [row[1] for row in result]

    plt.figure()
    plt.bar(categories, totals)
    plt.xlabel("Category")
    plt.ylabel("Total Amount (₹)")
    plt.title("Category-wise Expense Report")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def monthly_chart():
    cursor.execute("""
        SELECT DATE_FORMAT(date, '%Y-%m') AS month,
        SUM(amount) FROM expenses
        GROUP BY month ORDER BY month
    """)
    result = cursor.fetchall()

    if not result:
        print("⚠ No data to display!")
        return

    months = [row[0] for row in result]
    totals = [row[1] for row in result]

    plt.figure()
    plt.plot(months, totals, marker='o')
    plt.xlabel("Month")
    plt.ylabel("Total Expense (₹)")
    plt.title("Monthly Expense Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main Menu
def menu():
    while True:
        print("\n----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Export to Excel")
        print("6. Expense Summary")
        print("7. Search by Date")
        print("8. Search by Category")
        print("9. Search by Date Range")
        print("10. Category Chart")
        print("11. Monthly Trend Chart")
        print("12. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            export_to_excel()
        elif choice == "6":
            summary_report()
        elif choice == "7":
            search_by_date()
        elif choice == "8":
            search_by_category()
        elif choice == "9":
            search_by_date_range()
        elif choice == "10":
            category_chart()
        elif choice == "11":
            monthly_chart()
        elif choice == "12":
            cursor.close()
            conn.close()
            print("Goodbye!")
            break        
        else:
            print("Invalid choice! Enter number 1-12")




menu()
