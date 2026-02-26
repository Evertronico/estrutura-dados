def calcular_quadrado(numero):
    
    return numero ** 2

valor_inserido = float(input("Digite um número: "))

resultado = calcular_quadrado(valor_inserido)

print(f"O quadrado de {valor_inserido} é {resultado}")