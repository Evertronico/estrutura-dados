'''
    3. Implemente manualmente uma estrutura de lista sequencial (simulando vetor), sem utilizar métodos prontos de listas Python.

    A estrutura deve permitir:

        Inserção em uma posição específica

        Remoção de um elemento (com deslocamento manual dos elementos)

        Busca sequencial

        Exibição dos elementos
'''

def inserir(lista, valor, posi):
    if posi < 0 or posi > len(lista):
        print("Posição inválida!")
        return
    
    lista += [None]  
    
    # dr
    for i in range(len(lista) - 1, posi, -1):
        lista[i] = lista[i - 1]
    
    lista[posi] = valor
    print(f"Valor {valor} inserido na posição {posi} com sucesso!")

def remover(lista, posi):
    if posi < 0 or posi >= len(lista):
        print("Posição inválida!")
        return
    
    valor_removido = lista[posi]
    
    # es
    for i in range(posi, len(lista) - 1):
        lista[i] = lista[i + 1]
    
    lista[:] = lista[:len(lista) - 1]
    
    print(f"Valor {valor_removido} removido da posição {posi} com sucesso!")

def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


def exibir(lista):
    if len(lista) == 0:
        print("A lista está vazia.")
    else:
        print("Elementos na lista sequencial:")
        for i in range(len(lista)):
            print(f"Posição [{i}] -> Valor: {lista[i]}")


def menu():
    print('=' * 50)
    print('||    <<<<<<<<<<<<MENU DE OPÇÕES>>:>>>>>>>>>    ||')
    print('||    1) -INSERIR EM POSIÇÃO ESPECÍFICA....:    ||')
    print('||    2) -REMOVER DE POSIÇÃO ESPECÍFICA....:    ||')
    print('||    3) -BUSCA SEQUENCIAL.................:    ||')
    print('||    4) -EXIBIR...........................:    ||')
    print('||    5) -SAIR.............................:    ||')
    print('=' * 50)

def main():
    Lsequencial = []
    
    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)
        
        if opcao == "1":
            valor = int(input("Infofrme o valor para inserir: "))
            pos = int(input("Informe a posição para inserir: "))
            inserir(Lsequencial, valor, pos)
            
        elif opcao == "2":
            pos = int(input("Informe a posição para remover: "))
            remover(Lsequencial, pos)
            
        elif opcao == "3":
            valor = int(input("Informe o valor para buscar: "))
            indice = busca_sequencial(Lsequencial, valor)
            if indice != -1:
                print(f"O valor {valor} foi encontrado na posição {indice}.")
            else:
                print("NÃO existe esse valor na lista.")
                
        elif opcao == "4":
            exibir(Lsequencial)
            
        elif opcao == "5":
            print("Saindo...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
