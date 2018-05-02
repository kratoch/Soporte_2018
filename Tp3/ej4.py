import pymysql


conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "SELECT * FROM personas WHERE DNI=%s"
cur.execute(query, 23456789)


for row in cur.fetchall():
    print("Nombre: %s \n Fecha de Nacimiento: %s \n DNI: %s \n Altura: %s" % (row[1], str(row[2]), str(row[3]), str(row[4])))


conn.commit()
cur.close()
conn.close()
