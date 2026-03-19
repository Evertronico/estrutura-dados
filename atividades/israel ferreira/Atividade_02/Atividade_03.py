'''
        Exercício 3 – Inserção Ordenada de Dados
    Implemente uma função que insira valores em uma lista mantendo a ordenação crescente, simulando um sistema que organiza automaticamente dados numéricos.
    Requisitos:
    * Lista deve permanecer ordenada após cada inserção
    * Encontrar posição correta manualmente
    * Deslocar elementos sem usar insert()
    * Não utilizar sort()
    * Implementar função reutilizável

'''
# Lista ordenada
dados = []

def inserir_ordenado(valor):
    # Se a lista estiver vazia, apenas adiciona
    if len(dados) == 0:
        dados.append(valor)
        return
    
    # Encontrar posição correta
    posicao = 0
    while posicao < len(dados) and dados[posicao] < valor:
        posicao += 1
    
    # Deslocar elementos manualmente
    dados.append(0)  # cria espaço no final
    for i in range(len(dados)-1, posicao, -1):
        dados[i] = dados[i-1]
    
    # Inserir valor na posição correta
    dados[posicao] = valor

def listar_dados():
    if len(dados) == 0:
        return ["Lista vazia."]
    return dados[:]

# Menu interativo
while True:
    print('=' * 50)
    print('||    <<<<<<<<<<<MENU DE DADOS>>>>>>>>>>>    ||')
    print('||    1) -INSERIR VALOR..................:    ||')
    print('||    2) -LISTAR VALORES.................:    ||')
    print('||    3) -SAIR...........................:    ||')
    print('=' * 50)

    opcao = input("- ")
    print("-"*50)

    if opcao == "1":
        valor = int(input("Digite um número: "))
        inserir_ordenado(valor)
        print(f"Valor {valor} inserido com sucesso!")
    elif opcao == "2":
        lista = listar_dados()
        print("Lista ordenada:", lista)
    elif opcao == "3":
        print("Saindo do sistema de dados...")
        break
    else:
        print("Opção inválida. Tente novamente.")