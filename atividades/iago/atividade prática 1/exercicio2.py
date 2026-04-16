def inserir(lista, valor):
    lista.append(valor)

def buscar(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return True
    return False

def remover(lista, valor):
    if buscar(lista, valor):
        lista.remove(valor)
        print("Elemento removido.")
    else:
        print("Elemento não encontrado.")

def exibir(lista):
    if len(lista) == 0:
        print("Lista vazia.")
    else:
        for elemento in lista:
            print(elemento)

lista = []

while True:
    print("\n1 - Inserir")
    print("2 - Remover")
    print("3 - Buscar")
    print("4 - Exibir")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = int(input("Digite o valor: "))
        inserir(lista, valor)

    elif opcao == "2":
        valor = int(input("Digite o valor: "))
        remover(lista, valor)

    elif opcao == "3":
        valor = int(input("Digite o valor: "))
        if buscar(lista, valor):
            print("Elemento encontrado.")
        else:
            print("Elemento não encontrado.")

    elif opcao == "4":
        exibir(lista)

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")