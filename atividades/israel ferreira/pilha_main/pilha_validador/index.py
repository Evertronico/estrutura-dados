from verificador import verificadorExpressao

# cria um objeto do verificador
verificador = verificadorExpressao()

# testa varias expressões matemáticas
print(verificador.verificar("(1 + 2) * (3 + 4)"))  # True
print(verificador.verificar("((1 + 2) * (3 + 4)"))  # False
print(verificador.verificar("(1 + 2) * (3 + 4))"))  # False
print(verificador.verificar("((1 + 2) * (3 + 4))"))  # True
print(verificador.verificar("((1 + 2) * (3 + 4)) + (5 - 6)"))  # True
print(verificador.verificar("((1 + 2) * (3 + 4)) + (5 - 6"))  # False
print(verificador.verificar("((1 + 2) * (3 + 4)) + 5 - 6)"))  # False

