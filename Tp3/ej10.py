import pymysql


conn = pymysql.connect(
    host="127.0.0.1", port=3307, user="root",
    passwd="1234", db="soporte2018"
)
print(conn)

cur = conn.cursor()
query = "SELECT * FROM personas LEFT JOIN personapeso ON personas.IdPersona = " \
        "personapeso.IdPersona WHERE personapeso.IdPersona IS NOT NULL UNION " \
        "SELECT * FROM personas " \
        "RIGHT JOIN personapeso ON personas.IdPersona = personapeso.IdPersona"


cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)


conn.commit()
cur.close()
conn.close()
