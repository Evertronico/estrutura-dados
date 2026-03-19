# Exercício 2 – Controle de Estoque com Validação de Regras
# Implemente um sistema de controle de estoque para uma loja. Cada produto deve possuir nome e quantidade disponível.
# Requisitos:
# Utilizar lista de estruturas (dicionário ou lista composta)
#  * Implementar entrada de produto (adicionar ou atualizar quantidade) x
#  * Implementar saída de produto com validação de estoque x
#  * Impedir retirada maior que a quantidade disponível x
#  * Implementar busca de produto pelo nome x
#  * Exibir todos os produtos x
        
def cadastrarProduto(lista):
    lista.append(criar_obj_tarefa())

def procuraCod(lista,valor):
    for i in range(len(lista)):
       if lista[i]["cod"] == valor:
           return i
    return -1

def procuraProduto(lista,valor):
    for i in range(len(lista)):
       if lista[i]["produto"] == valor:
           return i
    return -1

def criar_obj_tarefa():
    cod = int(input('Digite o codigo..: '))
    produto = input('Digite o produto..: ')
    quantidade = int(input('Digite a quantidade ..: '))
    print('='*30)
    return {"cod": cod, "produto": produto, "quantidade": quantidade}

def saida(codigo, quantidade):
    posicao = procuraCod(produtos,codigo)
    if produtos[posicao]["quantidade"] >= quantidade:
        print('Saida com sucesso')
        produtos[posicao]["quantidade"] -= quantidade
    else:
        print('Quantidade maior que o estoque')

produtos = []
opcao = None
print()
while (opcao != 0):

    print('1 - Cadastrar um produto')
    print('2 - Saída de produto')
    print('3 - Listar produtos')
    print('4 - Buscar produtos')
    opcao = int(input('Informe uma opção ou zero para sair..: '))
    print('='*30)

    if(opcao == 1):
        print('='*30)
        cadastrarProduto(produtos)
        print('='*30)

    elif(opcao == 2):
        print('='*30)
        codigo = int(input('Codigo do produto para saída: '))
        quantidade = int(input('quantidade do produto para saída: '))
        saida(codigo, quantidade)
        print('='*30)

    elif(opcao == 3):
        print('='*30)
        for index,produto in enumerate(produtos):
            print(f'{index} - {produto}')
        print('='*30)

    elif(opcao == 4):
        print('='*30)
        nome = input('Nome do produto: ')
        posicao = procuraProduto(produtos, nome)
        if posicao >= 0 :
            print(produtos[posicao])
        else: 
            print('Produto não existe')
        print('='*30)

    elif(opcao == 0):
        break
    else:
        print('='*30)
        print(f'A opção selecionada {opcao} não existe.')
        continue
