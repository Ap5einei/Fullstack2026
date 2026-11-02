#
# Python and SQLite operations
#
 
import sqlite3

# here we create a connection to database
# it uses connect() command
connection = sqlite3.connect("testdatabase.db")
print("Hello SQLite")

# after connection has been established...
# connection is given commands
# execute() is used to run SQL commands
# this command creates a table to database

# https://www.w3schools.blog/create-table-sqlite

# This command destroys table if it is already there
connection.execute("""
DROP TABLE IF EXISTS Accounts;
""")

# commit() command forces database to carry out the order
connection.commit()

# this creates a table from scratch
connection.execute("""
CREATE TABLE Accounts
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SALDO REAL,
CREDIT REAL,
INFO TEXT
);
""")

connection.commit()

# this command closes connection to database
connection.close()


#
# You can add records to database
#
# record is effective same as element in a list
connection = sqlite3.connect("testdatabase.db")
print("Add records")


# https://www.w3schools.blog/insert-query-sqlite
connection.execute("""
INSERT INTO Accounts (ID, NAME, SALDO, CREDIT, INFO) 
VALUES (1, 'Aku', 313.00, 0.00, '');
""")

connection.execute("""
INSERT INTO Accounts (ID, NAME, SALDO, CREDIT, INFO)
VALUES (2, "Iines", 123.45, 1200.00, "friend of Aku");
""")

connection.commit()

connection.close()

print("Add records END")

#
# You can read all records of a table
#
connection = sqlite3.connect("testdatabase.db")
print("Read all records")

# cursor() is used to fetch data from database
cursor = connection.cursor()
cursor.execute("SELECT * FROM Accounts")
#rows = cursor.fetchall()
rows = cursor.fetchmany(100)

print("Accounts contents:")
for row in rows:
    print("ID = ", row[0]) # id
    print("NAME = ", row[1]) # name
    print("SALDO = ", row[2]) # saldo
    print("CREDIT = ", row[3]) # credit
    print("INFO = ", row[4]) # info
    print("\n")

cursor.close()
connection.close()

print("Read all records END")

#
# You can read one record at the time from a table
#
connection = sqlite3.connect("testdatabase.db")
print("Read one record")

cur = connection.cursor()
#cur.execute("SELECT * FROM Accounts WHERE name=?", ('Aku',))
#cur.execute("SELECT * FROM Accounts WHERE id=?", (2,))
cur.execute("SELECT * FROM Accounts WHERE id=? AND name=?", (2,'Iines'))
data = cur.fetchone()
print("koe")
print("ID = ", data[0]) # id
print("NAME = ", data[1]) # id
print("SALDO = ", data[2]) # id
print("CREDIT = ", data[3]) # id
print("INFO = ", data[4]) # id
print("\n")

"""
for record in data:
    print("koe")
    print("ID = ", record[0]) # id
    print("NAME = ", record[1]) # id
    print("SALDO = ", record[2]) # id
    print("CREDIT = ", record[3]) # id
    print("INFO = ", record[4]) # id
    print("\n")
"""

cur.close()
connection.close()

print("Read one record END")

#
# You change a record
#

connection = sqlite3.connect("testdatabase.db")
print("change one record")

connection.execute(
    """
    UPDATE Accounts 
    SET credit=? 
    WHERE name=? 
    """,
    (12345.56,'Aku',)
)

connection.commit()

# check the contents of Accounts table
cursor = connection.cursor()
cursor.execute("SELECT * FROM Accounts")
rows = cursor.fetchall()

print("Accounts contents:")
for row in rows:
    print("ID = ", row[0]) # id
    print("NAME = ", row[1]) # name
    print("SALDO = ", row[2]) # saldo
    print("CREDIT = ", row[3]) # credit
    print("INFO = ", row[4]) # info
    print("\n")

cursor.close()
connection.close()

print("change one records END")


#
# delete from database
#

connection = sqlite3.connect("testdatabase.db")
print("delete one records")


connection.execute(
    """
    DELETE FROM Accounts 
    WHERE name=? 
    """,
    ('Aku',)
)

connection.commit()

# check that Aku was deleted
cursor = connection.cursor()
cursor.execute("SELECT * FROM Accounts")
rows = cursor.fetchall()

print("Accounts contents:")
for row in rows:
    print("ID = ", row[0]) # id
    print("NAME = ", row[1]) # name
    print("SALDO = ", row[2]) # saldo
    print("CREDIT = ", row[3]) # credit
    print("INFO = ", row[4]) # info
    print("\n")

cursor.close()
connection.close()

print("delete one records END")

# TASK OOP-08
# 
# Easy task:
# Add more functions to bank
#
# Hard task:
# Change bank to use SQLite database
# 
# If you find tasks too hard, then study using udemy
#

