import sqlite3
conexao = sqlite3.connect('banco_teste.db')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, nota INTEGER)')
conexao.commit()

conexao.close()
alunos_cadastrado = []
