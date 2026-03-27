def adicionar(alunos, nome):
    alunos.append(nome)


def buscar(alunos, nome):
    for i in range(len(alunos)):
        if alunos[i] == nome:
            return i
    return -1


def remover(alunos, nome):
    pos = buscar(alunos, nome)

    if pos == -1:
        print("Aluno não encontrado.")
        return

    # deslocamento manual
    for i in range(pos, len(alunos) - 1):
        alunos[i] = alunos[i + 1]

    alunos.pop()  # remove último duplicado


def exibir(alunos):
    for aluno in alunos:
        print(aluno)


# Teste
alunos = []

adicionar(alunos, "Ana")
adicionar(alunos, "Carlos")
adicionar(alunos, "Maria")

remover(alunos, "Carlos")

exibir(alunos)