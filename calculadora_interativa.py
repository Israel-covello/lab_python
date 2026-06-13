print("=== SISTEMA DE PRECIFICAÇÃO ===")

# 1 - Entrada de dados.
nome_produto = input("Insira o nome do produto: ")

# Conversão para decimal.
custo_compra = float(input("Custo do produto: "))
preco_venda = float(input("Preço de venda planejado: "))

# 2 - Regra de processamento.
lucro_bruto = preco_venda - custo_compra
margem_percentual = (lucro_bruto / preco_venda) * 100

# 3 - Decisão
print("\n--- Relatório Financeiro de", nome_produto, "---")

if margem_percentual >= 30:
    print("Status APROVADO! Margem de", round(margem_percentual, 2),"%")
elif margem_percentual >= 20:
    print("Status ATENÇAÕ! Margem de", round(margem_percentual, 2),"%")
else:
    print("Satatus REPROVADO! Margem baixa de", round(margem_percentual),"%")
