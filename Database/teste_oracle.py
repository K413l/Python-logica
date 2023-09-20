import oracledb

con =  oracledb.connect(user='pf0313', 
                        password='professor#23', 
                        dsn='oracle.fiap.com.br/orcl')

cursor = con.cursor()

cursor.execute("select * from empregado")

registros = cursor.fetchall()
for reg in registros:
    print (reg)


cursor.close()
con.close()