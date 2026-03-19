# Função que cria o TDA de notas
# Retorna a estrutura que representa o estado interno do TDA
def criar_tda_notas():
    return []

# Operação do TDA responsável por inserir uma nota
# O usuário interage com os dados apenas por meio desta operação
def inserir_nota(tda, nota):
    tda.append(nota)

# Operação do TDA que processa os dados para gerar informação
# A média representa uma informação derivada dos dados armazenados
def calcular_media(tda):
    return sum(tda) / len(tda)

# Criação do TDA
notas = criar_tda_notas()

# Uso das operações definidas para manipular o TDA
inserir_nota(notas, 7.0)
inserir_nota(notas, 8.5)
inserir_nota(notas, 6.0)

# Exibição da informação gerada pelo TDA
print(calcular_media(notas))
