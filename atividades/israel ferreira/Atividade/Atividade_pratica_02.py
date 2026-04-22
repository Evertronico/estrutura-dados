'''
    2. Implemente um TAD de Lista de Números, utilizando funções em Python.

    O TAD deve oferecer as seguintes operações:

        Inserir elemento

        Remover elemento

        Buscar elemento (retornar se existe ou não)

        Exibir todos os elementos
'''

def inserir(lista, valor):
    lista.append(valor)
    print("Valor inserido com sucesso!")

def remover(lista, valor):
    encontrado = False
    tamanho = len(lista)

    for i in range(tamanho):
        if lista[i] == valor:
            # desloca os elementos para a esquerda
            for j in range(i, tamanho - 1):
                lista[j] = lista[j + 1]
            # reduz o tamanho da lista manualmente
            lista[:] = lista[:tamanho - 1]
            encontrado = True
            print(f"Valor {valor} removido!")
            break

    if not encontrado:
        print("Valor não encontrado na lista.")


def buscar(lista, valor):
    if valor in lista:
        return True
    else:
        return False

def exibir(lista):
    if len(lista) > 0:
        print("Elementos na lista:")
        for i in range(len(lista)):
            print(f"[{i}] -> {lista[i]}")
    else:
        print("Lista vazia.")

def menu():
    print('=' * 50)
    print('||    <<<<<<<<<<<<MENU DE OPÇÕES>>:>>>>>>>>>    ||')
    print('||    1) -INSERIR ELEMENTO.................:    ||')
    print('||    2) -REMOVER ELEMENTO.................:    ||')
    print('||    3) -BUSCAR ELEMENTO..................:    ||')
    print('||    4) -EXIBIR TODOS OS ELEMENTOS........:    ||')
    print('||    5) -SAIR.............................:    ||')
    print('=' * 50)

def main():
    lista_dados = []
    
    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)
        
        if opcao == "1":
            valor = int(input("Inserir Valor: "))
            inserir(lista_dados, valor)
            
        elif opcao == "2":
            valor = int(input("Remover Valor: "))
            remover(lista_dados, valor)
            
        elif opcao == "3":
            valor = int(input("Buscar Valor: "))
            encontrado = buscar(lista_dados, valor)
            if encontrado:
                print(f"O valor {valor} existe na lista.")
            else:
                print("NÃO existe esse valor na lista.")
                
        elif opcao == "4":
            exibir(lista_dados)
            
        elif opcao == "5":
            print("Saindo...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
