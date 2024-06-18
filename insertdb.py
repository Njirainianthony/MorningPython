import sqlite3

conn = sqlite3.connect('example.db')
print("Database connected successfully")

conn.execute("INSERT INTO Employee VALUES(1,'Mike','Tyson',57,200000.00,'Manager')")
conn.execute("INSERT INTO Employee VALUES(2,'Conor','McGregor',34,135000.00,'Admin')")
conn.execute("INSERT INTO Employee VALUES(3,'Riddick','Bowe',55,100000.00,'Secretary')")
conn.execute("INSERT INTO Employee VALUES(4,'Evander','Holyfield',56,80000.00,'HR Manager')")
conn.execute("INSERT INTO Employee VALUES(5,'Lennox','Lewis',57,90000.00,'Receptionist')")
conn.execute("INSERT INTO Employee VALUES(6,'Thomas','Hearn',46,190000.00,'Consultant')")

conn.commit()
print("Successfully inserted into Employee table")


