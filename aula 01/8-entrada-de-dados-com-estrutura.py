# a estrutura permite trabalhar com quantidade variável de dados.
notas = []
notas.append(float(input("Nota 1: ")))
notas.append(float(input("Nota 2: ")))
notas.append(float(input("Nota 3: ")))

media = sum(notas) / len(notas)
print("Média:", media)
