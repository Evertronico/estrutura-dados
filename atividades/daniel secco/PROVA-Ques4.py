class Node:
    def __init__(self, valor = None):
        self.valor = valor
        self.proximo = None

class ListaEncad:
    def __init__(self):
        self.cabeca = None

    
    def inserir(self, valor):
        novo_node = Node(valor)
        if not self.cabeca:
            self.cabeca = novo_node
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_node

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False
    

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" ->")
            atual = atual.proximo

        print("None")

listaEncad = ListaEncad()
listaEncad.inserir(10)
listaEncad.inserir(234)
listaEncad.exibir()
