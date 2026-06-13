# 1 - Entrada de dados 
nome_produto = "Notebook Lenovo"
custo_compra = 2000
preco_venda = 2300

# 2 - Processamento
lucro_bruto = preco_venda - custo_compra
margem_percentual = (lucro_bruto / preco_venda) * 100

# 3 -A saída 
print("--- Relatório Financeiro ---")
print("Produto:", nome_produto)
print("Lucro Bruto: R$", lucro_bruto)
print("Margem de Lucro:", round(margem_percentual, 2),"%")

# 4 - A decisão (inteligência do negócio)
print("--- Análise Automática ---")

if margem_percentual >= 30:
    print("Status: AROVADO! Margem de lucro excelente.")
elif margem_percentual >= 20:
    print("Status: ATENÇÃO! Margem aceitavel, mas requer volume de vendas.")
else:
    print("Status: BROQUEADO! Margem de lucro baixa. Rever fornecedor.")
