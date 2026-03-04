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
estoque = []

def inserir():
    inserir = {}
    print('=' * 50)
    print('INICIANDO CADASTRO DE PRODUTOS')
    inserir['nome']   = input('Nome--------------------------: ')
    inserir['qtd']    = int(input('Quantidade----------------: '))
    inserir['preco']  = float(input('Preço-------------------: '))

    estoque.append(inserir.copy)
    print('=' * 50)
    print('Cadastro feito com sucesso!👍😁👍')
    print('=' * 50)

# OPÇÕES
def opcoes ():
    while True:
        print('=' * 50)
        print('||    <<<<<<<<<<<<MENU DE OPÇÕES>>:>>>>>>>>>    ||')
        print('||    1) -INSERIR PRODUTOS.................:    ||')
        print('||    2) -REMOVER PRODUTOS NOME............:    ||')
        print('||    3) -LISTAR PRODUTOS..................:    ||')
        print('||    4) -CALCULAR ESTOQUE.................:    ||')
        print('=' * 50)

        opcaoP = int(input('Informe a opção desejada: '))
        if   opcaoP == 1:
            inserir()
        elif opcaoP == 2:
            remover()
        elif opcaoP == 3:
            listar()
        elif opcaoP == 4:
            calcular()
        elif opcaoP == 5:
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente')

def listar():
    print('Listagem de Funcionários')
    for produtos in estoque:
        print(produtos)


# funçao remover
def remover():
    if estoque == 0:
        print('Não foi possivel remover\n Tente novamente.')
    else:
        for i in estoque:
            del estoque[i]
    return print('PRODUTO REMOVIDO COM SUCESSO👍')

# função calcular
def calcular():
    return print('EM ANALISE')

opcoes()