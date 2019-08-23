import MySQLdb

db= MySQLdb.connect(host='127.0.0.1',
                    user='root',
                    passwd='',
                    db='pessoa')

cur = db.cursor()

def cadastro(ide,nam,ag,paws):
    cur.execute("INSERT INTO pessoa.cliente (id_cliente, nome, idade, pw) VALUES ( %s, %s, %s, SHA1(%s))", (ide, nam, ag, paws))
    db.commit()
    print("Cadastro efetuado com sucesso!")
