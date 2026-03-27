class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


# criação manual da lista
n1 = No(5)
n2 = No(10)
n3 = No(15)

n1.proximo = n2
n2.proximo = n3

# percorrendo a estrutura
atual = n1

while atual is not None:
    print(atual.dado)
    atual = atual.proximo