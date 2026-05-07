# Nó da lista duplamente encadeada
class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.anterior = None
        self.proximo = None