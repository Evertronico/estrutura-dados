# Estrutura linear com ordenação implícita por posição.
notas = [8.5, 7.0, 9.2, 6.8]

# Inserção no final com append().
# Em listas Python, essa operação é amortizada O(1).
# Representa crescimento dinâmico da estrutura.
notas.append(10.0)

# Inserção em posição específica.
# Conceito: deslocamento interno de elementos (custo O(n)).
notas.insert(2, 8.0)

# Remoção por valor.
# O método percorre a lista até encontrar o elemento.
notas.remove(6.8)

# Remoção por índice.
# Também implica reorganização interna da estrutura.
del notas[0]

print(notas)