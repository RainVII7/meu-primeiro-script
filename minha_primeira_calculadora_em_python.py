# Minha primeira calculadora em Python

print("===> CALCULADORA DO MESTRE <===")

# Pede os números ao mestre
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Pede a operação ao mestre
print("Escolha a operação, mestre:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação, mestre: ")

# Faz o cálculo do mestre
if opcao == "1":
    resultado = numero1 + numero2
    print("O resultado é:", resultado)

elif opcao == "2":
    resultado = numero1 - numero2
    print("O resultado é:", resultado)

elif opcao == "3":
    resultado = numero1 * numero2
    print("O resultado é:", resultado)

elif opcao == "4":
    if numero2 == 0:
        print("Erro: não é possível dividir por zero, mestre!")
    else:
        resultado = numero1 / numero2
        print("O resultado é:", resultado)

else:
    print("Opção inválida, mestre!")

