#Exercício 2 – Controle de Estoque com Validação de Regras
#Implemente um sistema de controle de estoque para uma loja. Cada produto deve possuir nome e quantidade disponível.
#Requisitos:
#Utilizar lista de estruturas (dicionário ou lista composta)
# * Implementar entrada de produto (adicionar ou atualizar quantidade)
# * Implementar saída de produto com validação de estoque
# * Impedir retirada maior que a quantidade disponível
# * Implementar busca de produto pelo nome
#* Exibir todos os produtos

produtos = []

def adicionarOuAtualizarProduto(nome, quantidade):
    if nome == '' or quantidade < 0:
        print("Nome e quantidade devem ser válidos")
        return
    
    i = 0
    encontrado = False
    while i < len(produtos):
        if produtos[i]["nome"] == nome:
            produtos[i]["quantidade"] += quantidade
            print(f"Produto '{nome}' atualizado para {produtos[i]['quantidade']} unidades")
            encontrado = True
            break
        i += 1
    
    if not encontrado:
        produtos.append({"nome": nome, "quantidade": quantidade})
        print(f"Produto '{nome}' adicionado com {quantidade} unidades")

def retirarProduto(nome, quantidade):
    if quantidade <= 0:
        print("Quantidade deve ser maior que zero")
        return
    
    i = 0
    while i < len(produtos):
        if produtos[i]["nome"] == nome:
            if produtos[i]["quantidade"] >= quantidade:
                produtos[i]["quantidade"] -= quantidade
                print(f"Retiradas {quantidade} unidades de '{nome}'")
            else:
                print(f"Erro: Estoque insuficiente. Disponível: {produtos[i]['quantidade']} unidades")
            return
        i += 1
    
    print(f"Produto '{nome}' não encontrado")

def buscarProduto(nome):
    i = 0
    while i < len(produtos):
        if produtos[i]["nome"] == nome:
            print(f"Produto encontrado: {produtos[i]['nome']} - Quantidade: {produtos[i]['quantidade']}")
            return
        i += 1
    print(f"Produto '{nome}' não encontrado")

def exibirTodosProdutos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado\n")
        return
    
    print("\n=== ESTOQUE ATUAL ===\n")
    i = 0
    while i < len(produtos):
        print(f"Produto: {produtos[i]['nome']} - Quantidade: {produtos[i]['quantidade']}")
        i += 1
    print()


adicionarOuAtualizarProduto("Notebook", 5)
adicionarOuAtualizarProduto("Mouse", 20)
adicionarOuAtualizarProduto("Teclado", 15)

exibirTodosProdutos()

retirarProduto("Mouse", 5)
exibirTodosProdutos()

retirarProduto("Mouse", 20)

buscarProduto("Notebook")
buscarProduto("Monitor")

adicionarOuAtualizarProduto("Mouse", 10)
exibirTodosProdutos()