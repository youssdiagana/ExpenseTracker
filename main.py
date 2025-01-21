import streamlit as st
from database import create_database, insert_expense, fetch_expenses, delete_expense
from visualization import plot_expenses_by_category, plot_expenses_by_date

# Ensure the database exists
create_database()


def main():
    st.title("Expense Tracker")
    st.write("Track your daily expenses easily!")

    # Input form for adding expenses
    st.header("Add New Expense")
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Groceries", "Transport", "Utilities", "Entertainment", "Other"])
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    description = st.text_input("Description (Optional)")

    if st.button("Add Expense"):
        insert_expense(str(date), category, amount, description)
        st.success("Expense added successfully!")

    # Display all expenses
    st.header("All Expenses")
    expenses = fetch_expenses()

    if not expenses:
        st.write("No expenses found.")
    else:
        for expense in expenses:
            st.write(
                f"ID: {expense[0]}, Date: {expense[1]}, Category: {expense[2]}, "
                f"Amount: ${expense[3]:.2f}, Description: {expense[4]}"
            )

            # Add delete button for each expense
            if st.button(f"Delete {expense[0]}"):
                delete_expense(expense[0])
                st.success(f"Deleted expense with ID {expense[0]}")
                st.experimental_rerun()  # Refresh the app to update the list of expenses

    # Visualization section
    st.header("Visualize Expenses")
    if expenses:
        if st.button("Show Expense Distribution by Category"):
            plot_expenses_by_category(expenses)
        if st.button("Show Expenses by Date"):
            plot_expenses_by_date(expenses)
    else:
        st.write("Add some expenses to see visualizations!")


if __name__ == "__main__":
    main()