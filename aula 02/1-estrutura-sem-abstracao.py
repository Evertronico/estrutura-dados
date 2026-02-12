# Criação direta de uma lista para armazenar notas
# Aqui temos apenas uma estrutura de dados, sem abstração
notas = []

# Inserção manual de valores na estrutura
# Cada valor representa um dado numérico bruto
notas.append(7.0)
notas.append(8.5)
notas.append(6.0)

# Processamento direto dos dados para gerar uma informação
# A média é uma informação obtida a partir dos dados
media = sum(notas) / len(notas)

# Saída da informação calculada
print(media)
