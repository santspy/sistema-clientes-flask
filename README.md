# Sistema de Clientes - Meu Primeiro Projeto Fullstack (Fazendo de forma 100% autônoma)

## A História por Trás do Código

Recentemente participei de um bate-papo para uma vaga de Dev Júnior (Python & Frontend). O gestor e o RH foram muito transparentes: disseram que buscavam alguém "cru", mas com muita sede de aprender e se desenvolver junto com a empresa. 

Em vez de apenas esperar pela próxima etapa ou pelo teste técnico de braços cruzados, decidi provar essa vontade na prática. Peguei os requisitos da vaga (Python, Banco de Dados, APIs e Frontend) e fui estudar a fundo como essas tecnologias se conectam no mundo real. O resultado é este mini projeto que fiz. 

Construí tudo de forma autônoma, escrevendo linha por linha, pesquisando a solução para os erros de sintaxe, entendendo a lógica de rotas e fazendo o Backend conversar com o Frontend. Ainda estou no início da minha jornada codando realmente sozinho, mas este código representa o meu comprometimento e a minha vontade em aprender as bases da programação de verdade, fugindo do copia e cola.

## Tecnologias que Aprendi e Utilizei

* **Backend:** Python + Flask (Criação de uma API REST para servir os dados).
* **Banco de Dados:** SQLite + SQL (Criação de tabelas, inserção com `INSERT` e consulta com `SELECT`).
* **Frontend:** HTML + JS (Uso da função `fetch()` para consumir a API e renderizar a lista dinamicamente).
* **Versionamento:** Git e GitHub.

## Como o Sistema Funciona

1. **Banco de Dados:** Um script inicial (`setup_banco.py`) cria um banco de dados SQLite local (`restaurante.db`) e insere alguns clientes de teste com seus respectivos status de pagamento.
2. **Backend:** O arquivo principal (`app.py`) usa o Flask para abrir uma conexão com o banco de dados e cria uma rota `GET /clientes` que devolve os dados em formato JSON.
3. **Frontend:** A página `index.html` possui um botão que, ao ser clicado, aciona uma função em JavaScript. Essa função faz uma requisição HTTP para a API, recebe o JSON e injeta a lista de clientes na tela do navegador.

## Como Rodar Localmente

Se você quiser testar o código na sua máquina, siga os passos abaixo:
1. Clone este repositório:
   ```bash
   git clone https://github.com/santspy/sistema-clientes-flask.git
   ````

  Instale o Flask:
   
  ````bash
  pip install flask
````
  Crie e popule o banco de dados:
  ````bash
  python setup_banco.py
  ````
  Inicie o servidor:
  ````bash
  python app.py
  ````
  Abra o navegador e acesse `http://127.0.0.1:5000/.`



