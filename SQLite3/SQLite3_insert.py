import sqlite3

# Connect to a database if it exists or create a new one
connection = sqlite3.connect('employees.db')
# Create a table (column)
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        hiringDate TEXT NOT NULL
    );
''')
connection.commit()

# Insert data into a table

name = input('Enter a name:')
position = input('Enter a position:')
date = input('Enter a date in the format yyyy-mm-dd:')

cursor.execute("INSERT INTO Employees VALUES (?, ?, ?, ?)",
               (1, name, position, date))
connection.commit()

# create another row

name = input('Enter a name:')
position = input('Enter a position:')
date = input('Enter a date in the format yyyy-mm-dd:')

cursor.execute("INSERT INTO Employees VALUES (?, ?, ?, ?)",
               (2, name, position, date))
connection.commit()
