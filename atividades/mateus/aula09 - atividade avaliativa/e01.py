# Exercício 1 – Cadastro de Alunos com Operações Básicas
# Implemente um sistema para gerenciamento de alunos de uma turma utilizando listas em Python. O sistema deve permitir o controle completo dos alunos cadastrados.
# Requisitos:
#  * Armazenar os alunos em uma lista x
#  * Implementar função para adicionar aluno x
#  * Implementar função para buscar aluno pelo nome (sem usar in ou index) x
#  * Implementar função para remover aluno manualmente (sem remove) x
#  * Exibir todos os alunos cadastrados x

alunos = []

def add(lista,nome):
    lista.append(nome)

def procura(lista,valor):
    for i in range(len(lista)):
       if lista[i] == valor:
           return i
    return -1

def remover(lista, valor):
    posicao = procura(lista,valor)
    if(posicao == -1):
        return
    for i in range(posicao, len(lista)-1):
        lista[i] = lista[i+1]
    lista.pop()

def listar(lista):
    for i in lista:
        print(i)
opcao = None
while (opcao != 0):

    print('1 - Cadastrar um aluno')
    print('2 - Buscar aluno')
    print('3 - Remover aluno')
    print('4 - Listar alunos')
    opcao = int(input('Informe uma opção ou zero para sair..: '))
    print('='*30)

    if(opcao == 1):
        print('='*30)
        aluno = input('Informe nome : ')
        add(alunos, aluno)
        print('='*30)
    elif(opcao == 2):
        print('='*30)
        aluno = input('Informe nome para buscar : ')
        id = procura(alunos, aluno);
        if id >= 0 :
            print(alunos[id])
        else: 
            print('Aluno não existe')
        print('='*30)
    elif(opcao == 3):
        print('='*30)
        aluno = input('Informe nome para remover : ')
        remover(alunos,aluno)
        print('='*30)

    elif(opcao == 4):
        print('='*30)
        listar(alunos)
        print('='*30)
    elif(opcao == 0):
        break
    else:
        print('='*30)
        print(f'A opção selecionada {opcao} não existe.')
        continue