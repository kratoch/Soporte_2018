import pymysql
import datetime

conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "INSERT INTO personas(IdPersona, Nombre, FechaNacimiento, DNI, Altura) VALUES (%s, %s, %s, %s, %s)"
cur.execute(query, (2, 'Pedro', datetime.date(1990, 12, 10), 34570987, 175))
print("Persona cargada exitosamente!")

conn.commit()
cur.close()
conn.close()



