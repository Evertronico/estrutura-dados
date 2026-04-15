'''
Exercício 1 – Cadastro de Alunos com Operações Básicas
Implemente um sistema para gerenciamento de alunos de uma turma utilizando listas em Python. O sistema deve permitir o controle completo dos alunos cadastrados.
Requisitos:
 * Armazenar os alunos em uma lista
 * Implementar função para adicionar aluno
 * Implementar função para buscar aluno pelo nome (sem usar in ou index)
 * Implementar função para remover aluno manualmente (sem remove)
 * Exibir todos os alunos cadastrados
 '''
alunos = []

def adicionar_aluno(lista, nome):
    lista.append(nome)
    print(f"Aluno '{nome}' cadastrado com sucesso!")


def buscar_aluno(lista, nome):
    for i in range(len(lista)):
        if lista[i] == nome:
            return i
    return -1

def remover_aluno(lista, nome):
    pos = buscar_aluno(lista, nome)

    if pos == -1:
        print("Aluno não encontrado!")
        return lista
    for i in range(pos, len(lista) - 1):
        lista[i] = lista[i + 1]

    nova_lista = []
    for i in range(len(lista) - 1):
        nova_lista.append(lista[i])

    print(f"Aluno '{nome}' removido com sucesso!")
    return nova_lista

def exibir_alunos(lista):
    print("\n📋 Lista de alunos:")
    if len(lista) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for i in range(len(lista)):
            print(f"{i} - {lista[i]}")


while True:
    print("\nGERENCIAMENTO DE ALUNOS ")
    print("1 - Adicionar aluno")
    print("2 - Buscar aluno")
    print("3 - Remover aluno")
    print("4 - Exibir alunos")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("\nCadastro de Aluno")
        nome = input("Digite o nome do aluno: ")
        adicionar_aluno(alunos, nome)

    elif opcao == "2":
        print("\n Buscar Aluno")
        nome = input("Digite o nome do aluno que deseja buscar: ")
        pos = buscar_aluno(alunos, nome)

        if pos != -1:
            print(f"Aluno encontrado na posição {pos}")
        else:
            print("Aluno não encontrado!")

    elif opcao == "3":
        print("\nRemover Aluno")
        nome = input("Digite o nome do aluno que deseja remover: ")
        alunos = remover_aluno(alunos, nome)

    elif opcao == "4":
        exibir_alunos(alunos)

    elif opcao == "0":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida! Tente novamente.")