# 💸 Expense Tracker

A simple and interactive web app built with **Streamlit** that lets you log, manage, and visualize your daily expenses by category.

🔗 **Live Demo:** [expensetrackerbyyouss.streamlit.app](https://expensetrackerbyyouss.streamlit.app/)

---

## Features

- **Add Expenses** – Log expenses with a date, category, amount, and optional description
- **View Expenses** – See a full list of all recorded expenses in one place
- **Delete Expenses** – Remove individual entries by ID
- **Visualize Spending** – Generate charts to understand your spending habits:
  - 🥧 **Pie Chart** – Expense distribution by category
    - 📊 **Bar Chart** – Total expenses grouped by date

    ---

    ## Categories

    Expenses can be assigned to the following categories:

    - Groceries
    - Transport
    - Utilities
    - Entertainment
    - Other

    ---

    ## Tech Stack

    | Tool | Purpose |
    |------|---------|
    | [Streamlit](https://streamlit.io/) | Web app framework & UI |
    | [SQLite](https://www.sqlite.org/) | Local database for storing expenses |
    | [Matplotlib](https://matplotlib.org/) | Data visualization (pie & bar charts) |
    | [Pandas](https://pandas.pydata.org/) | Data handling (dependency) |

    ---

    ## Project Structure

    ```
    ExpenseTracker/
    ├── main.py           # Main Streamlit app — UI and app logic
    ├── database.py       # SQLite database operations (create, insert, fetch, delete)
    ├── visualization.py  # Matplotlib chart functions (pie chart & bar chart)
    └── requirements.txt  # Python dependencies
    ```

    ---

    ## Getting Started

    ### Prerequisites

    - Python 3.8+
    - pip

    ### Installation

    1. **Clone the repository:**

    ```bash
    git clone https://github.com/youssdiagana/ExpenseTracker.git
    cd ExpenseTracker
    ```

    2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    3. **Run the app:**

    ```bash
    streamlit run main.py
    ```

    4. Open your browser and go to `http://localhost:8501`

    ---

    ## Usage

    1. Use the **"Add New Expense"** form to enter a date, category, amount, and description
    2. Click **"Add Expense"** to save it to the local database
    3. View all your expenses listed below the form
    4. Click **"Delete [ID]"** to remove a specific expense
    5. Under **"Visualize Expenses"**, click the chart buttons to explore your spending patterns

    ---

    ## Author

    **youssdiagana** – [GitHub Profile](https://github.com/youssdiagana)

    ---

    ## License

    This project is open source and available under the [MIT License](LICENSE).
