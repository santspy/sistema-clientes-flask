import sqlite3

print("--- CONSTRUINDO O BANCO DE DADOS ---")

# 1. Cria um arquivo chamado 'restaurante.db'
conexao = sqlite3.connect('restaurante.db')
cursor = conexao.cursor()

# 2. Cria a nossa tabela (como se fosse a aba do Excel) com as colunas id, nome e status
cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, status TEXT)')

# 3. Limpa a tabela para não duplicar dados se você rodar isso duas vezes
cursor.execute('DELETE FROM clientes')

# 4. Usa o comando SQL INSERT para salvar o João e a Maria
cursor.execute("INSERT INTO clientes (nome, status) VALUES ('João', 'Pendente')")
cursor.execute("INSERT INTO clientes (nome, status) VALUES ('Maria', 'Pago')")
cursor.execute("INSERT INTO clientes (nome, status) VALUES ('Carlos', 'Pendente')") # Adicionei o Carlos para provar que funciona!

# 5. Salva e fecha
conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso! Verifique se apareceu o arquivo restaurante.db na sua pasta.")