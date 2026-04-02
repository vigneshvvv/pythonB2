import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Vignesh333#",
    database= "javatrainingpro" 
)

cur  = conn.cursor()

cur.execute("select * from books")

result = cur.fetchall()

for row in result:
    print(row)

cur.close()
conn.close()
