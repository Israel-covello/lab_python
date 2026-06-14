import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

# Chave de acesso (API Key).
minha_chave = os.getenv("CHAVE_GOOGLE")

# Conectando com o servidor.
client = genai.Client(api_key=minha_chave)

print("=== TERMINAL ESTRATÉGICO CONECTADO ===")
print("Digite 'sair' para encerrar.\n")

# Loop de Interações.
while True:
    pergunta = input("Você: ")
    
    if pergunta.lower() == 'sair':
        print("Desconectando... Até logo!")
        break
    
    print("Processando...")
    
    # Enviando o pedido e aguardando a resposta para o servidor.
    resposta = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=pergunta
    )
    
    # Exibindo a resposta em formato de texto.
    print("Gemini:", resposta.text)
    print("-" * 40)

