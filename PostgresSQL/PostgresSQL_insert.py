# pip3 install psycopg2-binary

import psycopg2

# Connect to the database
# The following data MUST be replaced with YOUR database data
connection = psycopg2.connect(
    dbname='railway',
    user='postgres',
    password='Y4EVahgoeOcJHhyEsi2m',
    port='7126',
    host='containers-us-west-32.railway.app'
)

# Create Employees table
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        position VARCHAR(255) NOT NULL,
        hiringDate DATE NOT NULL
    );
''')
connection.commit()

# Ask the user to enter employee data
name = input("Enter the name of the employee: ")
position = input("Enter the position of the employee: ")
hiringDate = input("Enter the hiring date (YYYY-MM-DD): ")

# Insert employee data into the database
cursor.execute("INSERT INTO Employees (name, position, hiringDate) VALUES (%s, %s, %s)",
               (name, position, hiringDate))
connection.commit()
