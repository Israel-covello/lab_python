import sqlite3
from datetime import datetime


# Função para inserir dados no Banco
def salvar_produto(nome, custo, venda, margem):
    
    # Captura a data de hoje automaticamente
    # O strftime('%Y-%m-%d') formata a data no padrão Americano
    data_hoje = datetime.now().strftime('%Y-%m-%d')

    # Conecta ao banco
    conexao = sqlite3.connect('compras.db')
    cursor = conexao.cursor()
    
    # Comando SQL para inserir dados
    # O '?' é um buraco que preenchemos com os dados reais logo abaixo
    comando_sql = "INSERT INTO produtos (nome, custo, venda, margem, data_registro) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(comando_sql, (nome, custo, venda, margem, data_hoje))
    
    # Salva e fecha
    conexao.commit()
    conexao.close()
    print(f"Produto '{nome}' registrado em {data_hoje} com sucesso!")

# Teste: Chamando a função passando os dados do produto
salvar_produto("Ração Premium", 150.00, 200.00, 25.0)
