# Criação do TDA representado por uma estrutura linear
def criar_tda():
    return []

# Operação do TDA responsável por inserir valores
def inserir(tda, valor):
    tda.append(valor)

# Operação do TDA que analisa os dados para gerar informação
def maior(tda):
    return max(tda)

# Instanciação do TDA
tda = criar_tda()

# Inserção de dados no TDA por meio da operação definida
inserir(tda, 1)
inserir(tda, 10)
inserir(tda, 8)
inserir(tda, 1024)
inserir(tda, 17)
inserir(tda, 38)

# Exibição da informação obtida a partir dos dados
print(maior(tda))
