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

# Update employee data
id_to_update = input("Enter the ID of the employee you want to update: ")
new_position = input("Enter the new position for this employee: ")
cursor.execute(
    "UPDATE Employees SET position = %s WHERE id = %s",
    (new_position, id_to_update)
)
connection.commit()


# Select and display all employees
cursor.execute("SELECT * FROM Employees")
employees = cursor.fetchall()
print(employees)


# Delete employee data
id_to_delete = input("Enter the ID of the employee you want to delete: ")
cursor.execute(
    "DELETE FROM Employees WHERE id = %s",
    (id_to_delete,)
)
