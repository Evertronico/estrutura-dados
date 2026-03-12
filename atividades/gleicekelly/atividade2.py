# Atividade 2 — Busca Sequencial
# Implemente uma função chamada:
# busca_sequencial(lista, valor)
# A função deve percorrer a lista e retornar:
# o índice do elemento encontrado
# -1 caso o valor não esteja presente.
# Não utilize:
# index()
# in

def buscaSequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

dados = ["Gleice", "Marilena", "Wesley", "Bryan"]
busca = "Marilena"

print("O valor " + busca + " foi encontrado no indice: ", buscaSequencial(dados, busca))