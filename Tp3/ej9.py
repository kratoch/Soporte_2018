'''Ejercicio 9
Hacer un programa Python para acceder a la tabla Personas y PersonaPeso y
buscar el registro de una persona identificada por su DNI, mostrar los datos de la
persona y de su historial de peso.'''
import pymysql
import datetime

conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "SELECT * FROM personas WHERE DNI=%s"

if cur.execute(query, 34570987):
    rows = cur.fetchall()
    for row in rows:
        print(row[1])
        query2 = "SELECT * FROM personapeso WHERE IdPersona=%s"
        if cur.execute(query2, row[0]):
            rows1 = cur.fetchall()
            print("Pesajes:")
            for row1 in rows1:
                print("Fecha: %s       Peso: %s " % (row1[1], row1[2]))
        else:
            print('no posee registros de peso')

else:
    print('no existe persona con ese DNI')

conn.commit()
cur.close()
conn.close()
