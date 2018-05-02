import pymysql

conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "select * from personas"
cur.execute(query)

rows = cur.fetchall()
if rows is not None:
    for row in rows:
        print("Nombre: %s \n Fecha de Nacimiento: %s \n DNI: %s \n Altura: %s" % (row[1], str(row[2]), str(row[3]), str(row[4])))
else:
    print("No existen elementos en la tabla")
