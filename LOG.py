import MySQLdb
import flask
from flask import request
from cad import cadastro
db= MySQLdb.connect(host='127.0.0.1',
                    user='root',
                    passwd='',
                    db='pessoa')
cur= db.cursor()

id=input("Informe seu cpf: ")
    name = input("Informe seu nome: ")
    age = input("Informe seu idade: ")
    sen=input("Informe uma senha: ")
    ver=input("Informe novamente a senha: ")
    cur.execute('''select id_cliente from pessoa.cliente where id_cliente=%s''', (id,))
    check=cur.fetchone()
    
    if sen==ver:
        if check is None:
            cadastro(id,name,age,sen)
        else:
            print("Cadastro já existente")
            cur.execute('''#select pw from pessoa.cliente where pw=(SHA1(%s))''', (sen,))
            verf=cur.fetchone()
            if verf is None:
                print("senha errada")
            else:
                print(verf)
                print("Login efetuado")

    else:
        print("Você informou senhas distintas!")
        login()
        return 1


#def login():
        #    if request.method=="POST":
        #username = request.form['username']
        #password = request.form['password']
        #cur.execute('''sele"ct id_cliente from pessoa.cliente where id_cliente=%s''', (username,))
        #check=cur.fetchone()

        #if check is None:
        #   print("Não existe")
        #else:
            #cur.execute('''select pw from pessoa.cliente where pw=(SHA1(%s))''', (password,))