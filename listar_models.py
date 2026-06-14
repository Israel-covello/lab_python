import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
minha_chave = os.getenv("CHAVE_GOOGLE")

# Consulta models disponivel do Google para integrar no meu_assitente
client = genai.Client(api_key=minha_chave)

print("--- Consultando o Catálogo Oficial ---")
for modelo in client.models.list():
    print(modelo.name)
