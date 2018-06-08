import pymysql
import datetime

conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "UPDATE personas SET Nombre = %s, FechaNacimiento = %s, DNI = %s, Altura = %s WHERE IdPersona = %s"
cur.execute(query, ('Francisco', datetime.date(1990, 12, 10), 34570987, 175, 1))


for row in cur.fetchall():
    print("Nombre: %s \n Fecha de Nacimiento: %s \n DNI: %s \n Altura: %s" % (row[1], str(row[2]), str(row[3]), str(row[4])))


conn.commit()
cur.close()
conn.close()
