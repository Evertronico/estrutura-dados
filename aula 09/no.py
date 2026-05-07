# Representa um nó da lista duplamente encadeada
class No:
    def __init__(self, dado):
        self.dado = dado          # valor armazenado
        self.proximo = None       # referência para o próximo nó
        self.anterior = None      # referência para o nó anterior