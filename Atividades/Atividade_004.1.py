'''
Atividade Aula prática 4:
    Exercício 4.1
    Crie uma função que receba um número e retorne seu quadrado.    
'''
def calcular_quadrado(a):
    return a * a

print("=" *50)
print("Calcule o quadrado de qualquer numero")
numero = int(input('Informe um numero: '))
resultado = calcular_quadrado(numero)

# Saida e Informação
print("=" *50)
print(f'O quadrado de {numero} é: {resultado}')