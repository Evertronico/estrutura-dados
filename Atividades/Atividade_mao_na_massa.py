'''
    ATIVIDADE prática - Mão na massa

    Problema

    Desenvolver um sistema que permita:

    1 - Inserir produtos em uma lista.

    2 - Remover produtos pelo nome.

    3 - Listar todos os produtos.

    4 - Calcular o valor total do estoque.

    Cada produto deve ser representado por um dicionário com nome, quantidade e preço.'
'''
'''
    ATIVIDADE prática - Mão na massa

    Problema

    Desenvolver um sistema que permita:

    1 - Inserir produtos em uma lista.

    2 - Remover produtos pelo nome.

    3 - Listar todos os produtos.

    4 - Calcular o valor total do estoque.

    Cada produto deve ser representado por um dicionário com nome, quantidade e preço.'
'''

produtos = []  

def inserir(nome, quantidade, preco):
    if quantidade < 0 or preco <= 0:
        raise ValueError("Valores invalidos")
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    produtos.append(produto)

def remover(nome):
    for p in produtos:
        if p["nome"].lower() == nome.lower(): # converter maiúsculos em minúsculos
            produtos.remove(p)
            return True
    else:
        return False

def listar():
    return produtos[:]

def calcular_total():
    return sum(p["quantidade"] * p["preco"] for p in produtos)

while True:
    print('=' * 50)
    print('||    <<<<<<<<<<<<MENU DE OPÇÕES>>:>>>>>>>>>    ||')
    print('||    1) -INSERIR PRODUTO..................:    ||')
    print('||    2) -REMOVER PRODUTO..................:    ||')
    print('||    3) -LISTAR  PRODUTO..................:    ||')
    print('||    4) -TOTAL   PRODUTO..................:    ||')
    print('||    5) -SAIR.............................:    ||')
    print('=' * 50)

    opcaoP = input("- ")
    print("-"*50)
    if opcaoP == "1":
        nome = input("Nome: ")
        qtd = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        inserir(nome, qtd, preco)
    elif opcaoP == "2":
        nome = input("Nome: ")
        remover(nome)
    elif opcaoP == "3":
        for p in listar():
            print(p)
    elif opcaoP == "4":
        print(calcular_total())
    elif opcaoP == "5":
            print('Saindo...')
            break
    else:
            print('Opção inválida. Tente novamente')

