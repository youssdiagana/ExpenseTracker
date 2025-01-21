import matplotlib.pyplot as plt
import streamlit as st

# Pie chart: Expense distribution by category
def plot_expenses_by_category(expenses):
    categories = [expense[2] for expense in expenses]
    amounts = [expense[3] for expense in expenses]

    category_totals = {}
    for category, amount in zip(categories, amounts):
        category_totals[category] = category_totals.get(category, 0) + amount

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(
        category_totals.values(),
        labels=category_totals.keys(),
        autopct='%1.1f%%',
        startangle=140
    )
    ax.set_title("Expense Distribution by Category")

    # Display in Streamlit
    st.pyplot(fig)

# Bar chart: Expenses per day
def plot_expenses_by_date(expenses):
    dates = [expense[1] for expense in expenses]
    amounts = [expense[3] for expense in expenses]

    date_totals = {}
    for date, amount in zip(dates, amounts):
        date_totals[date] = date_totals.get(date, 0) + amount

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(date_totals.keys(), date_totals.values(), color='skyblue')
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Expenses")
    ax.set_title("Expenses by Date")
    ax.set_xticks(range(len(date_totals.keys())))
    ax.set_xticklabels(date_totals.keys(), rotation=45)
    plt.tight_layout()

    # Display in Streamlit
    st.pyplot(fig)