import sqlite3

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

# List all data from a table
cursor.execute("SELECT * FROM Employees")
employees = cursor.fetchall()
print(employees)

# Update data in a table in this case it will change the position, of ID=2
cursor.execute("UPDATE Employees SET position = ? WHERE id = ?",
               ('camera', 2))
connection.commit()

# Delete data from a table (from the specified id)
# cursor.execute("DELETE FROM Employees WHERE id = ?", (1,))
# connection.commit()

# Mandatory in the case of SQLite, close the connection, after finishing operations
connection.close()
