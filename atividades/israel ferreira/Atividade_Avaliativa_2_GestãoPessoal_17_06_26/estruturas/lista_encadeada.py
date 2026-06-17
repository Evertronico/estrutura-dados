class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, dado):
        novo_no = No(dado)
        if not self.head:
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def buscar(self, criterio_func):
        atual = self.head
        while atual:
            if criterio_func(atual.dado):
                return atual.dado
            atual = atual.proximo
        return None

    def remover(self, criterio_func):
        atual = self.head
        anterior = None
        while atual:
            if criterio_func(atual.dado):
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.head = atual.proximo
                return atual.dado
            anterior = atual
            atual = atual.proximo
        return None

    def exibir(self):
        elementos = []
        atual = self.head
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        return elementos
