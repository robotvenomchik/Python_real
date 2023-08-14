import psycopg2

import pprint as p

DATABASE='test_db'
USER='root'
PASSWORD='root'
HOST='127.0.0.1'
PORT='55555'

connection=psycopg2.connect(
    database=DATABASE,
    user=USER,
    host=HOST,
    password=PASSWORD,
    port=PORT,

)

cursor=connection.cursor()

data=cursor.execute('SELECT 2+2 AS result;')
print(data)

cursor.execute("INSERT INTO instructors(name) VALUES('Marta');")
connection.commit()
cursor.close()
connection.close()