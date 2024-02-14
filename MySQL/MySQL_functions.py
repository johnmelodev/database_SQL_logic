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

# Insert data into the table based on user input

id1 = input("Enter the ID for the first employee: ")
name1 = input("Enter the name for the first employee: ")
position1 = input("Enter the position for the first employee: ")
hiringDate1 = input(
    "Enter the hiring date for the first employee (YYYY-MM-DD): ")

query = "INSERT INTO Employees VALUES (%s, %s, %s, %s)"
values1 = (id1, name1, position1, hiringDate1)

cursor.execute(query, values1)
connection.commit()

# List all data from the table after the update
cursor.execute("SELECT * FROM Employees")
employees = cursor.fetchall()
print(employees)

connection.close()
