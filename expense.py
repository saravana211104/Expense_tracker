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


# Main Menu
def menu():
    while True:
        print("\n----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")

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
            cursor.close()
            conn.close()
            print("Goodbye!")
            break        
        else:
            print("Invalid choice! Enter number 1-5")




menu()
