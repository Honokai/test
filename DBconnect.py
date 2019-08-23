import MySQLdb

db= MySQLdb.connect(host='127.0.0.1',
                    user='root',
                    passwd='',
                    db='pessoa')

cur = db.cursor()

cur.execute('SELECT * FROM pessoa.cliente')

for row in cur.fetchall():
    print(row)

db.close()