# Lista que vai armazenar os nomes dos alunos
alunos = []

# Função para adicionar um aluno
def adicionar_aluno(nome):
    alunos.append(nome)
    print(f"Aluno '{nome}' adicionado com sucesso!")

# Função para buscar aluno 
def buscar_aluno(nome):
    for i in range(len(alunos)):
        if alunos[i] == nome:
            print(f"Aluno '{nome}' encontrado na posição {i}.")
            return i
    
    print(f"Aluno '{nome}' não foi encontrado.")
    return -1

# Função para remover aluno manualmente
def remover_aluno(nome):
    posicao = buscar_aluno(nome)
    
    if posicao == -1:
        print("Não foi possível remover.")
        return
    
    # Desloca os elementos para a esquerda
    for i in range(posicao, len(alunos) - 1):
        alunos[i] = alunos[i + 1]
    
    alunos.pop()
    print(f"Aluno '{nome}' removido com sucesso!")

# Função para listar alunos
def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nLista de alunos:")
    for i in range(len(alunos)):
        print(f"{i + 1} - {alunos[i]}")

# -------------------------
# MENU INTERATIVO
# -------------------------

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar aluno")
    print("2 - Buscar aluno")
    print("3 - Remover aluno")
    print("4 - Listar alunos")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Adicionar aluno
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        adicionar_aluno(nome)
    
    # Buscar aluno
    elif opcao == "2":
        nome = input("Digite o nome do aluno: ")
        buscar_aluno(nome)
    
    # Remover aluno
    elif opcao == "3":
        nome = input("Digite o nome do aluno: ")
        remover_aluno(nome)
    
    # Listar alunos
    elif opcao == "4":
        listar_alunos()
    
    # Sair do sistema
    elif opcao == "0":
        print("Saindo do sistema... até mais 👋")
        break
    
    # Caso o usuário digite algo inválido
    else:
        print("Opção inválida! Tente novamente.")