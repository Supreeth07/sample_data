import psycopg2

conn =(psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="12345678", port="5432"))

cur=conn.cursor()

with open('file.sql', 'r') as sql_file:
    sql_commands=sql_file.read()

cur.execute(sql_commands)

conn.commit()

cur.close()
conn.close()