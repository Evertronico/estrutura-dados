from busca_sequencial import busca_sequencial
from remocao_manual_por_indice import remover_posicao

def remover_valor(lista, valor):
    indice = busca_sequencial(lista, valor)
    if indice != -1:
        remover_posicao(lista, indice)

dados = [100, 200, 300, 400]
remover_valor(dados, 300)
print(dados)