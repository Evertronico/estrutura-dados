_lista = []
_tamanho = 0


def inserir_posicao(elemento, posicao):
    global _lista, _tamanho
    elemento = float(elemento)
    posicao = int(posicao)
    
    if posicao < 0 or posicao > _tamanho:
        print(f"Posição inválida! Use de 0 a {_tamanho}")
        return False
    
    nova_lista = []
    
    for i in range(len(_lista)):
        if i == posicao:
            nova_lista = nova_lista + [elemento]
        nova_lista = nova_lista + [_lista[i]]
    
    if posicao == _tamanho:
        nova_lista = nova_lista + [elemento]
    
    _lista = nova_lista
    _tamanho += 1
    print(f"Elemento {elemento} inserido na posição {posicao}")
    return True


def remover(posicao):
    global _lista, _tamanho
    posicao = int(posicao)
    
    if posicao < 0 or posicao >= _tamanho:
        print(f"Posição inválida! Use de 0 a {_tamanho - 1}")
        return False
    
    elemento = _lista[posicao]
    nova_lista = []
    
    for i in range(len(_lista)):
        if i != posicao:
            nova_lista = nova_lista + [_lista[i]]
    
    _lista = nova_lista
    _tamanho -= 1
    print(f"Elemento {elemento} removido da posição {posicao}")
    return True


def buscar(elemento):
    elemento = float(elemento)
    posicao = -1
    
    for i in range(len(_lista)):
        if _lista[i] == elemento:
            posicao = i
            break
    
    if posicao != -1:
        print(f"Elemento {elemento} encontrado na posição {posicao}")
        return True
    else:
        print(f"Elemento {elemento} não encontrado")
        return False


def exibir():
    if _tamanho == 0:
        print("Lista vazia!")
    else:
        print("Elementos: ", end="")
        for i in range(len(_lista)):
            print(f"[{i}]={_lista[i]} ", end="")
        print()
        print(f"Total de elementos: {_tamanho}")


def limpar():
    global _lista, _tamanho
    _lista = []
    _tamanho = 0
    print("Lista limpa com sucesso!")


def menu():
    ativo = True
    
    while ativo:
        print("\n" + "=" * 50)
        print("Estrutura de lista sequencial (simulando vetor)")
        print("=" * 50)
        print("1. Inserir em posição específica")
        print("2. Remover por posição")
        print("3. Buscar elemento")
        print("4. Exibir lista")
        print("5. Limpar lista")
        print("0. Sair")
        print("=" * 50)
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                posicao = input("Digite a posição: ")
                elemento = input("Digite o elemento: ")
                inserir_posicao(elemento, posicao)
            
            case "2":
                posicao = input("Digite a posição a remover: ")
                remover(posicao)
            
            case "3":
                elemento = input("Digite o elemento a buscar: ")
                buscar(elemento)
            
            case "4":
                exibir()
            
            case "5":
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
