class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_final(self, valor):
        novo = Node(valor)

        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

    def buscar(self, valor):
        atual = self.inicio
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def exibir(self):
        atual = self.inicio
        while atual is not None:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

# Teste
lista = ListaEncadeada()
lista.inserir_final(10)
lista.inserir_final(20)
lista.inserir_final(30)

lista.exibir()