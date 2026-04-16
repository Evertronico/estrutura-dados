arrayDeNumeros = []
cont = 0
opcao = 0

def adicionar_numero(array, numero):
    return array + [numero]

while opcao != 4:
    
    while cont < 5:
        numero = int(input("Digite um numero: "))
        arrayDeNumeros = adicionar_numero(arrayDeNumeros, numero)
        cont += 1
    print("\n" + "=" * 50)
    print("Lista de numeros")
    print("=" * 50)
    print("1. Somar os números")
    print("2. Média dos números")
    print("3. Maior e menor número")
    print("0. Sair")
    print("=" * 50)
    opcao = input("Escolha uma opção: ")
    match opcao:
        case "1":
            soma = 0
            for numero in arrayDeNumeros:
                soma += numero
            print("A soma dos numeros é: ", soma)
        case "2":
            soma = 0
            for numero in arrayDeNumeros:
                soma += numero
            media = soma / len(arrayDeNumeros)
            print("A média dos numeros é: ", media)
        case "3":
            maior = arrayDeNumeros[0]
            menor = arrayDeNumeros[0]
            for numero in arrayDeNumeros:
                if numero > maior:
                    maior = numero
                if numero < menor:
                    menor = numero
            print("O maior numero é: ", maior)
            print("O menor numero é: ", menor)
        case "0":
            print("Saindo...")
            break
        case _:
            print("Opção inválida")

