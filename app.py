import sqlite3
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def pagina_inicial():
    return render_template('index.html')

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    # 1. Abre a porta da despensa (conecta no banco)
    conexao = sqlite3.connect('restaurante.db')
    
    # Esse comando mágico faz o SQLite entregar os dados como dicionários do Python
    conexao.row_factory = sqlite3.Row 
    cursor = conexao.cursor()

    # O SEU DESAFIO COMEÇA AQUI
    # 2. Você precisa usar o cursor.execute() para rodar um comando SQL.
    # O comando SQL para "Selecionar tudo da tabela clientes" é: SELECT * FROM clientes
    
    cursor.execute("SELECT * FROM clientes") 
    
    
    # 3. Pega todos os resultados que o SQL encontrou
    linhas = cursor.fetchall()
    conexao.close()

    # 4. Converte para o formato que a nossa API e o JS entendem
    clientes_db = [dict(linha) for linha in linhas]

    return jsonify(clientes_db)

if __name__ == '__main__':
    app.run(debug=True)