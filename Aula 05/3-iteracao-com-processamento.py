# Lista representando coleção homogênea de dados numéricos.
notas = [8.5, 7.0, 9.2, 6.8]

# Variável acumuladora para processamento sequencial.
soma = 0

# Iteração linear.
# Conceito: percurso sequencial típico de estruturas lineares (O(n)).
for nota in notas:
    soma += nota  # Processamento elemento a elemento.

# Uso da função len() para obter tamanho da estrutura.
# Reflete controle estrutural sobre cardinalidade da lista.
media = soma / len(notas)

print("Média da turma:", round(media, 2))