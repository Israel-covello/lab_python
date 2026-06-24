import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
from google import genai

# Carrega as credenciais seguras do cofre
load_dotenv()
minha_chave = os.getenv("CHAVE_GOOGLE")
client = genai.Client(api_key=minha_chave)

print("=== TERMINAL ESTRATÉGICO CONECTADO COM MEMÓRIA ===")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")
    
    if pergunta.lower() == 'sair':
        print("Desconectando e salvando sessão... Até logo!")
        break
    
    print("Processando...")
    
    # Consulta ao Fornecedor
    resposta = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=pergunta
    )
    
    texto_resposta = resposta.text
    
    print("Gemini:", texto_resposta)
    print("-" * 40)
    
    # ==========================================
    # A MÁGICA DA MEMÓRIA (O Trator)
    # ==========================================
    data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conexao = sqlite3.connect('compras.db')
    cursor = conexao.cursor()
    
    # Garante que a gaveta existe ANTES de salvar
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico_conversas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT,
            resposta TEXT,
            data_hora TEXT
        )
    ''')
    
    # Salva a conversa
    comando_sql = "INSERT INTO historico_conversas (pergunta, resposta, data_hora) VALUES (?, ?, ?)"
    cursor.execute(comando_sql, (pergunta, texto_resposta, data_hora_atual))
    
    conexao.commit()
    conexao.close()