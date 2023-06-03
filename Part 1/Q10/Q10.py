## Creating the SQL database
import sqlite3

""""
# Connect to SQLite database. If the database doesn't exist, it will be created
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL command to create a table
cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    position TEXT NOT NULL,
    hireDate TEXT NOT NULL
);
''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

## Add new data to database
# Connect to SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL command to insert data into the table
cursor.execute('''
INSERT INTO employees (name, department, position, hireDate)
VALUES ('John Doe', 'Engineering', 'Engineer', '2023-01-01');
''')

# Data to insert
data_to_insert = [
    ('Janes Doe', 'Marketing', 'Manager', '2022-05-01'),
    ('Alice Smith', 'Sales', 'Sales Representative', '2023-02-01'),
    # Add more tuples for more rows
]

# Execute a SQL command to insert data into the table
cursor.executemany('''
INSERT INTO employees (name, department, position, hireDate)
VALUES (?, ?, ?, ?);
''', data_to_insert)


# Commit the transaction
conn.commit()

# Close the connection
conn.close()



# Connect to SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL command to select all data from the table
cursor.execute('SELECT * FROM employees;')

# Fetch all results into a list
data = cursor.fetchall()

# Close the connection
conn.close()

# Print the data
for row in data:
    print(row)



#Execute function example
cursor.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        position TEXT NOT NULL
    );
''')

cursor.execute("INSERT INTO employees VALUES (1, 'John Doe', 'Engineering', 'Engineer')")

cursor.execute("SELECT * FROM employees")

cursor.execute("UPDATE employees SET name = 'Jane Doe' WHERE id = 1")

cursor.execute("DELETE FROM employees WHERE id = 1")

cursor.execute("DROP TABLE employees")


"""
