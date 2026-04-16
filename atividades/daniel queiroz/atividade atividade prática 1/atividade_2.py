_lista = []


def inserir(numero):
    global _lista
    numero = float(numero)
    _lista = _lista + [numero]
    print(f"Número {numero} inserido com sucesso!")


def remover(numero):
    global _lista
    numero = float(numero)
    nova_lista = []
    encontrado = False
    
    for i in range(len(_lista)):
        if _lista[i] != numero:
            nova_lista = nova_lista + [_lista[i]]
        else:
            encontrado = True
    
    if encontrado:
        _lista = nova_lista
        print(f"Número {numero} removido com sucesso!")
        return True
    else:
        print(f"Número {numero} não encontrado na lista!")
        return False


def buscar(numero):
    numero = float(numero)
    encontrado = False
    
    for i in range(len(_lista)):
        if _lista[i] == numero:
            encontrado = True
            break
    
    if encontrado:
        print(f"Número {numero} foi encontrado na lista!")
        return True
    else:
        print(f"Número {numero} não foi encontrado na lista!")
        return False


def exibir():
    if len(_lista) == 0:
        print("A lista está vazia!")
    else:
        print("Elementos da lista:", _lista)
        print(f"Total de elementos: {len(_lista)}")


def limpar():
    global _lista
    _lista = []
    print("Lista limpa com sucesso!")


def tamanho():
    return len(_lista)


def menu():
    ativo = True
    
    while ativo:
        print("\n" + "=" * 50)
        print("TAD de Lista de Números")
        print("=" * 50)
        print("1. Inserir número")
        print("2. Remover número")
        print("3. Buscar número")
        print("4. Exibir lista")
        print("5. Tamanho da lista")
        print("6. Limpar lista")
        print("0. Sair")
        print("=" * 50)
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                numero = input("Digite o número a inserir: ")
                inserir(numero)
            
            case "2":
                numero = input("Digite o número a remover: ")
                remover(numero)
            
            case "3":
                numero = input("Digite o número a buscar: ")
                buscar(numero)
            
            case "4":
                exibir()
            
            case "5":
                print(f"Tamanho da lista: {tamanho()}")
            
            case "6":
                confirmar = input("Tem certeza? (s/n): ")
                if confirmar.lower() == "s":
                    limpar()
            
            case "0":
                print("Encerrando o programa...")
                ativo = False
            
            case _:
                print("Opção inválida! Tente novamente.")


executando = True

while executando:
    menu()
    executando = False
