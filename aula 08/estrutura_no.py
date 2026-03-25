class No:
    def __init__(self, dado):
        # valor armazenado no nó
        self.dado = dado
        
        # referência para o próximo nó da lista
        self.proximo = None


# criando nós manualmente
n1 = No(10)
n2 = No(20)

# conectando os nós
n1.proximo = n2

print(n1.dado)
print(n1.proximo.dado)