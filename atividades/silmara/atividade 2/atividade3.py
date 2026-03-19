# Exercício 3 – Inserção Ordenada de Dados
# Implemente uma função que insira valores em uma lista mantendo a ordenação crescente, simulando um sistema que organiza automaticamente dados numéricos.
# Requisitos:
#  * Lista deve permanecer ordenada após cada inserção
#  * Encontrar posição correta manualmente
#  * Deslocar elementos sem usar insert()
#  * Não utilizar sort()
#  * Implementar função reutilizável

lista_ordenada = []

def inserir_ordenado(valor):
    posicao = 0
    while posicao < len(lista_ordenada) and lista_ordenada[posicao] < valor:
        posicao += 1
    
    lista_ordenada.append(None)
    for i in range(len(lista_ordenada) - 1, posicao, -1):
        lista_ordenada[i] = lista_ordenada[i-1]
    
    lista_ordenada[posicao] = valor

inserir_ordenado(12)
inserir_ordenado(14)
inserir_ordenado(34)
inserir_ordenado(89)
inserir_ordenado(1)

print(f'Lista final: {lista_ordenada}')