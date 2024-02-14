# pip3 install mysql-connector-python
import mysql.connector
# Connect to a database or create it
connection = mysql.connector.connect(
    user='root',
    password='StrongPassword123',
    host='localhost',
    database='academy'  # name of the database
)
# this database is created inside a server. you can access it through MySQLworkbench

# Create a table
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        id INT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        position VARCHAR(255) NOT NULL,
        hiringDate DATE NOT NULL
    );
''')

connection.commit()

# List all data from the table after the update
cursor.execute("SELECT * FROM Employees")
employees = cursor.fetchall()
print(employees)


# Update data in the table
query = "UPDATE Employees SET position = %s WHERE id = %s"
values = ('Senior Developer', 1)
cursor.execute(query, values)
connection.commit()

# Delete data from the table
cursor.execute("DELETE FROM Employees WHERE id = %s", (1,))
connection.commit()

# close the connection to the database
connection.close()
