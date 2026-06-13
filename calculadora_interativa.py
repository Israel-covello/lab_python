print("=== SISTEMA DE PRECIFICAÇÃO ===")
print("Dica: Digite 'sair' no nome do produto para fechar o sistema.\n")

# Comando de loop (roda para sempre)
while True:
    print("-" * 30) # Apenas imprime a linha tracejada

    # 1 - Entrada de dados
    nome_produto = input("Insira o nome do produto: ")

    # A regrada para parar (Botão de emergência)
    # .lower() transforma o que o usuário digitou em minúsculas para evitar erros (Sair, SAIR, sair)
    if nome_produto.lower() == 'sair':
        print("Sessão encerrada!")
        break # O "break" é o freio de mão que quebra o loop e finaliza o programa

    custo_compra = float(input("Insira o preço de custo: "))
    preco_venda = float(input("Insira o preço de venda planejado: "))

    # 2 - O Processamento
    lucro_bruto = preco_venda - custo_compra
    margem_percentual = (lucro_bruto / preco_venda) * 100

    # 3 - A decisão
    print("\n [ RESULTADO ]")
    if margem_percentual >= 30:
        print("Satatus: APROVADO! Margem de", round(margem_percentual, 2), "%")
    elif margem_percentual >= 20:
        print("Satatus ATENÇÃO! Margem baixa de", round(margem_percentual, 2), "%")
    else:
        print("Status: BLOQUEADO! Margem baixa de", round(margem_percentual, 2), "%")
    print("\n") # Pula uma linha antes de reiniciar o loop
