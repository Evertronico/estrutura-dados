class ListaSequencial:
    def __init__(self):
        self.itens = []

    def inserir(self, item):
        self.itens.append(item)

    def buscar(self, criterio_func):
        for item in self.itens:
            if criterio_func(item):
                return item
        return None

    def remover(self, criterio_func):
        for i, item in enumerate(self.itens):
            if criterio_func(item):
                return self.itens.pop(i)
        return None

    def exibir(self):
        return self.itens
