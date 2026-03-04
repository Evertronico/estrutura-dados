# Lista contendo dicionários.
# Demonstra heterogeneidade e modelagem de entidades reais.
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 6.0},
    {"nome": "Marina", "nota": 9.1}
]

# Nova lista para armazenar subconjunto filtrado.
# Conceito: construção de nova estrutura derivada.
aprovados = []

# Percurso completo da estrutura original.
for aluno in alunos:
    # Acesso indexado indireto via chave do dicionário.
    if aluno["nota"] >= 7:
        # Inserção dinâmica em nova lista.
        aprovados.append(aluno)

print("Aprovados:")
for aluno in aprovados:
    print(aluno["nome"])