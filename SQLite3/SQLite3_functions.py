import sqlite3

# Connect to or create a database


def connect_db(db_name):
    connection = sqlite3.connect(db_name)
    return connection

# Create a table


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE Employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            hiringDate TEXT NOT NULL
        );
    ''')
    connection.commit()

# Insert data into a table


def insert_employee(connection, id, name, position, hiringDate):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Employees VALUES (?, ?, ?, ?)",
                   (id, name, position, hiringDate))
    connection.commit()

# List all data from a table


def select_all_employees(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Employees")
    return cursor.fetchall()

# Update data in a table


def update_employee(connection, id, position):
    cursor = connection.cursor()
    cursor.execute("UPDATE Employees SET position = ? WHERE id = ?",
                   (position, id))
    connection.commit()

# How to delete data from a table


def delete_employee(connection, id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Employees WHERE id = ?", (id,))
    connection.commit()


# Using the functions
connection = connect_db('employees.db')

# Create a table
create_table(connection)

# Example of how to receive user data in your application and then pass it to the database
name = input('Enter a name:')
position = input('Enter a position:')
date = input('Enter a date in the format yyyy-mm-dd:')

insert_employee(connection, 1, name, position, date)
insert_employee(connection, 2, name, position, date)

# Example of using the table that searches and returns data from a table
print(select_all_employees(connection))  # Prints all employees

# Example of using the function to update data in a table
update_employee(connection, 2, 'Senior Developer')

# Example of how to return data that was returned from the database
# Prints all employees after the update
print(select_all_employees(connection))

# Example of using the function to delete a user
delete_employee(connection, 1)

# Example of using the table that searches and returns data from a table
# Prints all employees after the deletion
print(select_all_employees(connection))

# Mandatory, in the case of SQLite, close the connection, after finishing operations
connection.close()
