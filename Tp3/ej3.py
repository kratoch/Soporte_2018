import pymysql


conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "DELETE FROM personas WHERE IdPersona=%s"
cur.execute(query, 2)

conn.commit()
cur.close()
conn.close()


