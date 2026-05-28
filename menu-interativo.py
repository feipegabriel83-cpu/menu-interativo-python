# ENTRADE DE DADOS
primeiro = int(input("Digite o primeiro valor: "))
segundo = int(input("Digite o segundo valor: "))
opcao = 0

# MENU PRINCIPAL
while opcao != 5:
    print("""
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa
    """)

    # PROCESSAMENTO DAS OPÇÕES
    opcao = int(input("Digite sua opção: ").strip())
    if opcao == 1:
        print(f"{primeiro} + {segundo} = {primeiro + segundo}")
    elif opcao == 2:
        print(f"{primeiro} * {segundo} = {primeiro * segundo}")
    elif opcao == 3:
        if primeiro > segundo:
            print(f"O maior número é: {primeiro}")
        elif primeiro < segundo:
            print(f"O maior número é: {segundo}")
        else:
            print(f"Os dois números são iguais!")
    elif opcao == 4:
        primeiro = int(input("Novo primeiro valor: "))
        segundo = int(input("Novo segundo valor: "))
    elif opcao < 1 or opcao > 5:
        print(f"Opção inválida! Tente novamente")


print(f"Finalizado com sucesso!!")