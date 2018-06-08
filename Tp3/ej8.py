'''Ejercico 8
Hacer un Programa Python donde pueda insertar registros en PersonaPeso y
que valide que la persona existe y que no existe de esa persona un registro de fecha
posterior al que queremos ingresar . '''
import pymysql
import datetime

conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "SELECT * FROM personas WHERE IdPersona=%s"

idPersona = 2
fecha = datetime.date(2018, 3, 23)
peso = 90

if cur.execute(query, idPersona):
    query = "SELECT * FROM personapeso WHERE IdPersona=%s"
    cur.execute(query, 2)
    rows = cur.fetchall()

    for row in rows:
        if str(row[1]) > str(fecha):
            print('existe una fecha posterior de peso')
        else:
            query = "INSERT INTO personapeso(IdPersona, Fecha, Peso) VALUES (%s, %s, %s)"
            cur.execute(query, (idPersona, fecha, peso))
else:
    print('no existe persona con ese id')

conn.commit()
cur.close()
conn.close()
