import sqlite3

# Conecta ao banco (se o arquivo não existir, o SQLite cria ele agora)
conexao = sqlite3.connect('compras.db')

cursor = conexao.cursor()

# Cria a tabela de produtos (Comando SQL)
# Definimos os campos: ID (único), nome, custo, venda, margem e data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        custo REAL,
        venda REAL,
        margem REAL,
        data_registro TEXT 
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS historico_conversa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pergunta TEXT,
        resposta TEXT,
        data_hora TEXT                  
    )
''')

# Salva e fecha a conexão
conexao.commit()
conexao.close()

print("Arquitetura do banco criada com sucesso! Tabelas criadas 'compras.db' e 'historico_conversa' !")
