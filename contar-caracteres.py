while True:
    print("1. Contar caracteres (sem espaços)")
    print("2. Contar palavras")
    print("3. Sair")

    opcao = input("Informe a opção: ")

    if opcao == '1':
        print("Informe o texto: ")
        caracter = input()
        frase_sem_espacos = caracter.replace(" ", "")
        print(f"O tamanho é: {len(frase_sem_espacos)}")

    elif opcao == '2':
        print("Informe a frase: ")
        frase = input()
        quantidade_palavras = frase.split()
        print(f"Quantidade de palavras é: {len(quantidade_palavras)}")

    elif opcao == '3':
        print("Fechando sistema.")
        break

    else:
        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
