import random

# Geração de lista com 10.000 elementos.
# Demonstra capacidade de armazenamento dinâmico.
dados = [random.randint(1, 1000) for _ in range(10000)]

# Implementação manual de busca sequencial.
# Conceito: algoritmo linear aplicado a estrutura linear.
def busca(valor, lista):
    # enumerate permite acesso simultâneo ao índice e ao elemento.
    for i, elemento in enumerate(lista):
        # Comparação elemento a elemento (O(n)).
        if elemento == valor:
            return i  # Retorna índice (acesso posicional).
    return -1  # Valor sentinela indicando ausência.

# Busca de elemento existente.
resultado = busca(dados[5000], dados)

print("Índice encontrado:", resultado)