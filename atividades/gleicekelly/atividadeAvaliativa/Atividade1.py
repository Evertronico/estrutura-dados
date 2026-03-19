alunos = []

def adicionarAluno(nome):
    alunos.append(nome)
    print(f"Aluno(a) '{nome}' adicionado(a) com sucesso!")

def buscarAluno(nome):
    for i in range(len(alunos)):
        if alunos[i] == nome:
            return i
    return -1

def removerAluno(nome):
    posicao = buscarAluno(nome)

    if posicao != -1:
        for i in range(posicao, len(alunos) - 1):
            alunos[i] = alunos[i + 1]

        alunos.pop()
        print(f"Aluno(a) '{nome}' removido(a) com sucesso!")
    else:
        print("Aluno não encontrado. Não foi possível remover.")

def listarAlunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLista de alunos:")
        for i in range(len(alunos)):
            print(f"{i + 1}. {alunos[i]}")

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar aluno")
    print("2 - Buscar aluno")
    print("3 - Remover aluno")
    print("4 - Listar alunos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do aluno: ")
        adicionarAluno(nome)

    elif opcao == '2':
        nome = input("Digite o nome do aluno: ")
        pos = buscarAluno(nome)
        if pos != -1:
            print(f"Aluno(a) '{nome}' encontrado(a) na posição {pos}.")
        else:
            print("Aluno não encontrado.")

    elif opcao == '3':
        nome = input("Digite o nome do aluno: ")
        removerAluno(nome)

    elif opcao == '4':
        listarAlunos()

    elif opcao == '0':
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")