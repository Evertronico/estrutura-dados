'''
    Exercício 1 – Cadastro de Alunos com Operações Básicas
    Implemente um sistema para gerenciamento de alunos de uma turma utilizando listas em Python.
    O sistema deve permitir o controle completo dos alunos cadastrados.
    Requisitos:
    * Armazenar os alunos em uma lista
    * Implementar função para adicionar aluno
    * Implementar função para buscar aluno pelo nome (sem usar in ou index)
    * Implementar função para remover aluno manualmente (sem remove)
    * Exibir todos os alunos cadastrados

'''

alunos = []  

def adicionar(nome, idade, turma):
    aluno = {"nome": nome, "idade": idade, "turma": turma}
    alunos.append(aluno)

def remover(nome):
    for i in range(len(alunos)):
        if alunos[i]["nome"].lower() == nome.lower():
            del alunos[i]
            return True
    return False

def busca(nome):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return f"{nome} encontrado na lista!"
    return f"{nome} não está na lista."  

def listar():
    if len(alunos) == 0:
        return ["Não a alunos na lista"]
    return alunos[:]


while True:
    print('=' * 50)
    print('||    <<<<<<<<<<<<MENU DE OPÇÕES>>:>>>>>>>>>    ||')
    print('||    1) -ADICIONAR ALUNO..................:    ||')
    print('||    2) -BUSCAR ALUNO NOME................:    ||')
    print('||    3) -REMOVER ALUNO....................:    ||')
    print('||    4) -LISTAR ALUNOS....................:    ||')
    print('||    5) -SAIR.............................:    ||')
    print('=' * 50)

    opcaoP = input("- ")
    print("-"*50)
    if opcaoP == "1":
        nome  =       input("Nome:  ")
        idade =   int(input("Idade: "))
        turma =      (input("Turma: "))
        adicionar(nome, idade, turma)
    elif opcaoP == "2":
        nome = input("Nome: ")
        print(busca(nome, idade, turma))
    elif opcaoP == "3":
        nome = input("Nome: ")
        if remover(nome):
            print(f"{nome} removido com sucesso!")
        else:
            print(f"{nome} não encontrado.")
    elif opcaoP == "4":
        a = listar()
        for p in a:
           print(p)
    elif opcaoP == "5":
            print('Saindo...')
            break
    else:
            print('Opção inválida. Tente novamente')