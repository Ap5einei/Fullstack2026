import sqlite3

connection = sqlite3.connect(".\\testQQQ.db")

connection.execute("""
INSERT INTO Accounts (ID, NAME, SALDO, CREDIT, INFO) 
VALUES (1, 'Aku', 313.00, 0.00, '');
""")



# this command closes connection to database
connection.close()
