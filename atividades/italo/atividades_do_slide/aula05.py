def entrada():
    nome = input()
    preco = float(input())
    return nome, preco

def calcular(preco):
    return preco * 1.1

def mostrar(nome, preco, novo):
    print(nome)
    print(f"{preco:.2f}")
    print(f"{novo:.2f}")

n, p = entrada()
novo = calcular(p)
mostrar(n, p, novo)