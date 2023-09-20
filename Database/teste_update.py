import oracledb

con = oracledb.connect(user='pf0313',
                       password='professor#23',
                        dsn="oracle.fiap.com.br/orcl")

cur = con.cursor()

sql = '''insert into empregado(nome, salario)
        values(:nome, :sal)'''

dados = {'nome':'Joana','sal':8290}
con.execute(sql, dados)

con.commit()
cur.close()
con.close()