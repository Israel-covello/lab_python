import sqlite3

conexao = sqlite3.connect('compras.db')
cursor = conexao.cursor()

comando_sql = "SELECT * FROM produtos"
cursor.execute(comando_sql)

resultados = cursor.fetchall()

print("\n=== RELATÓRIO HISTÓRICO DE COMPRAS ===")
print("-" * 50)

for linha in resultados:
    id_prod, nome, custo, venda, margem, data = linha

    print(f"[{data}] {nome} | Custo: R$ {custo:.2f} | Margem: {margem}%")

print("-" * 50)

conexao.close()

