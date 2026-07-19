# ============================================================
# Project 14 - AI SQL Assistant
#
# File: database.py
#
# Purpose:
# This file creates a SQLite database and inserts sample
# employee data. It also prevents duplicate data insertion
# if the script is executed multiple times.
# ============================================================

# Import SQLite module
# SQLite is built into Python, so no installation is required.
import sqlite3


# ============================================================
# Connect to SQLite Database
# ============================================================

# If employees.db does not exist, SQLite creates it automatically.
connection = sqlite3.connect("employees.db")

# Cursor is used to execute SQL queries.
cursor = connection.cursor()


# ============================================================
# Create Employees Table
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    department TEXT NOT NULL,

    salary INTEGER,

    experience INTEGER,

    city TEXT

)
""")


# ============================================================
# Sample Employee Data
# ============================================================

employees = [

    ("Alice", "Engineering", 120000, 5, "Bangalore"),
    ("Bob", "HR", 70000, 3, "Pune"),
    ("Charlie", "Finance", 90000, 4, "Mumbai"),
    ("David", "Engineering", 150000, 7, "Hyderabad"),
    ("Eva", "Marketing", 80000, 2, "Delhi"),
    ("Frank", "Engineering", 135000, 6, "Bangalore"),
    ("Grace", "Finance", 95000, 5, "Pune"),
    ("Helen", "HR", 75000, 4, "Chennai"),
    ("Ian", "Marketing", 85000, 3, "Mumbai"),
    ("Jack", "Engineering", 160000, 8, "Bangalore")

]


# ============================================================
# Check Whether Data Already Exists
# ============================================================

# Count the number of rows present in the employees table.
cursor.execute("SELECT COUNT(*) FROM employees")

# fetchone() returns a tuple like (10,)
record_count = cursor.fetchone()[0]


# ============================================================
# Insert Sample Data (Only if Table is Empty)
# ============================================================

if record_count == 0:

    cursor.executemany(
        """
        INSERT INTO employees
        (name, department, salary, experience, city)

        VALUES (?, ?, ?, ?, ?)
        """,
        employees
    )

    print("✅ Sample employee data inserted successfully!")

else:

    print("ℹ️ Employee data already exists. Skipping insertion.")


# ============================================================
# Save Changes
# ============================================================

# Commit permanently saves all changes to the database.
connection.commit()


# ============================================================
# Read Employee Records
# ============================================================

print("\n📋 Employee Records:\n")

cursor.execute("SELECT * FROM employees")

employee_records = cursor.fetchall()

for employee in employee_records:
    print(employee)


# ============================================================
# Close Database Connection
# ============================================================

connection.close()

print("\n✅ Database setup completed successfully!")