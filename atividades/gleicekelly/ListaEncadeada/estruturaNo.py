class No:
    def __init__(self, valor):
        self.valor = valor
        self.proxima = None

#cria uma lista manual
n1 = No(18)
n2 = No(30)
n1.proxima = n2
n3 = No(42)
n2.proxima = n3

atual = n1
while atual is not None:
    print(atual.valor)
    atual = atual.proxima
