import MySQLdb
from LOG import login

db= MySQLdb.connect(host='127.0.0.1',
                    user='root',
                    passwd='',
                    db='pessoa')
login()
'''
#id=input("Informe o cpf: ")
#name=input("Informe o nome: ")
#age=input("Informe o idade: ")
#paw=input("Informe uma senha: ")

cur= db.cursor()

cur.execute("select id_cliente from pessoa.cliente where id_cliente=%s", (id,))
check=cur.fetchone()
'''
'''
if check is None:
    cur.execute("INSERT INTO pessoa.cliente (id_cliente, nome, idade, pw) VALUES ( %s, %s, %s, SHA1(%s));", (id, name, age, paw))
    #cur.execute("insert into pessoa.cliente (pw) values (SHA1('passwmene'))", paw)
    db.commit()
    print("Não exite, mas agora foi adicionado!")
else:
    print("Cadastro já existente, executar o login.")
    login()
'''

