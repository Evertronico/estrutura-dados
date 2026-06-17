class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None

    def consulta_primeiro(self):
        if not self.esta_vazia():
            return self.itens[0]
        return None

    def esta_vazia(self):
        return len(self.itens) == 0
    
    def exibir(self):
        return self.itens
