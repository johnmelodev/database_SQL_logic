# pip3 install psycopg2-binary

import psycopg2


def connect_db(dbname, user, password, port, host='localhost'):
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        port=port,
        host=host
    )
    return connection


def create_table(connection):
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


def insert_employee(connection, name, position, hiringDate):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Employees (name, position, hiringDate) VALUES (%s, %s, %s)",
        (name, position, hiringDate)
    )
    connection.commit()


def update_employee(connection, id, new_position):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE Employees SET position = %s WHERE id = %s",
        (new_position, id)
    )
    connection.commit()


def delete_employee(connection, id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Employees WHERE id = %s", (id,))
    connection.commit()


def list_employees(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Employees")
    return cursor.fetchall()


# Usage examples:
connection = connect_db('railway', 'postgres', 'Y4EVahgoeOcJHhyEsi2m',
                        '7126', 'containers-us-west-32.railway.app')


create_table(connection)

name = input("Enter the name of the employee: ")
position = input("Enter the position of the employee: ")
hiringDate = input("Enter the hiring date (YYYY-MM-DD): ")

insert_employee(connection, name, position, hiringDate)

id_to_update = input("Enter the ID of the employee you want to update: ")
new_position = input("Enter the new position for this employee: ")

update_employee(connection, id_to_update, new_position)

id_to_delete = input("Enter the ID of the employee you want to delete: ")

delete_employee(connection, id_to_delete)

print(list_employees(connection))

connection.close()
