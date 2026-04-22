'''
    1. Desenvolva um programa em Python que:

    Solicite ao usuário a entrada de 5 números inteiros

    Armazene os valores em uma estrutura de dados

        Exiba:

        A soma dos elementos

        A média

        O maior e o menor valor
'''

def main():
    numeros = []
    print("="*40)
    print("insira 5 números inteiros:")
    for i in range(5):
        valor = int(input(f"Digite o {i+1}º número: "))
        numeros.append(valor)
    
    soma = 0
    maior = numeros[0]
    menor = numeros[0]
    
    for n in numeros:
        soma += n
        
        if n > maior:
            maior = n
            
        if n < menor:
            menor = n
            
    media = soma / 5
    
    print("-" * 30)
    print(f"Soma dos elementos..: {soma}")
    print(f"Média dos elementos.: {media:.2f}")
    print(f"Maior valor.........: {maior}")
    print(f"Menor valor.........: {menor}")
    print("-" * 30)

if __name__ == "__main__":
    main()
