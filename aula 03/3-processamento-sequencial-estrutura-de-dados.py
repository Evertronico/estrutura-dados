# Estrutura de dados linear utilizada para armazenar múltiplos valores
# A lista organiza os dados de forma sequencial
notas = [6.0, 7.5, 8.0, 9.0]

# Variável acumuladora para o processamento dos dados
# Inicialmente representa um valor neutro para a soma
soma = 0

# Laço for utilizado para percorrer cada elemento da estrutura
# O processamento ocorre de forma sequencial
for nota in notas:
    # A cada iteração, um dado da estrutura é acessado
    soma += nota  # Processamento dos dados por acumulação

# Cálculo da média a partir dos dados processados
# A média representa uma informação gerada pelo algoritmo
media = soma / len(notas)

# Exibição da informação final obtida
print("Média:", media)
