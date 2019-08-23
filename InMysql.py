import MySQLdb

db= MySQLdb.connect(host='127.0.0.1',
                    user='root',
                    passwd='',
                    db='pessoa')

cur = db.cursor()

cur.execute('''INSERT INTO pessoa.cliente (id_cliente, nome, idade) VALUES ('27836', 'Jordan',1928-12-12),('156253', 'Mogran',1998-09-09)''')

db.commit()