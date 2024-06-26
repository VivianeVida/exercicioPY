def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '5':
            print("Obrigado por usar a calculadora. Até mais!")
            break
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                resultado = num1 + num2
                print(f"\nResultado: {num1} + {num2} = {resultado}")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"\nResultado: {num1} - {num2} = {resultado}")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"\nResultado: {num1} * {num2} = {resultado}")
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"\nResultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: divisão por zero!")
            else:
                print("Opção inválida. Por favor, escolha uma operação válida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

# Chama a função principal da calculadora
calculadora()
