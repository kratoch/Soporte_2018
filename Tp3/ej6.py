import pymysql

conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "select * from personas"
cur.execute(query)

lista = list(cur.fetchall())

for i in lista:
    print(i)

conn.commit()
cur.close()
conn.close()
