# Função para calcular a média entre duas notas.

def calcule_media(n1,n2):
    return  (n1 + n2) / 2


# Função para exibir o resultado

def mostre_resultado(nome, media):
    print(f"Aluno: {nome}")
    print(f"Media: {media}")

# Entrada de dados

# nome = input("Nome: ")
# nota1 = float(input("Primeira nota: "))
# nota2 = float(input("Segunda nota: "))

#implementar uma função para a entrada de dados

def recebe_dados_aluno():
    nome = input("Nome: ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    return nome,nota1,nota2

rs = recebe_dados_aluno()
nome = rs[0]
nota1 = rs[1]
nota2 = rs[2]

# calcula a média e exibe as inforações

media = calcule_media(nota1,nota2)

print(nome)
print(nota1)
print(nota2)
print(media)
# mostre_resultado(nome,media)


