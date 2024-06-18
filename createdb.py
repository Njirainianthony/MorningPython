import sqlite3


conn=sqlite3.connect('example.db')
print("Successfully connected to database")


conn.execute('''
CREATE TABLE Employee(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL,
POSITION TEXT NOT NULL
)''')

print("Table Employee created successfully")
conn.close()


