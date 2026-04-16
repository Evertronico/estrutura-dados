'''4. Implemente uma Lista Encadeada Simples em Python utilizando classes.'''

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, valor):
        no = Node(valor)

        if self.head is None:
            self.head = no
        else:
            atual = self.head

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = no

    def buscar(self, valor):
        atual = self.head
        
        i = 0

        while atual is not None:
            if atual.valor == valor:
                return i
            
            i += 1
            atual = atual.proximo

        return -1

    def exibir_lista(self):
        atual = self.head

        while atual is not None:
            print(atual.valor)

            atual = atual.proximo


lista = ListaEncadeada()

lista.inserir(5)
lista.inserir(8)
lista.inserir(2)
lista.inserir(4)
lista.inserir(6)
lista.inserir(8)

lista.exibir_lista()

n1 = 5
n1_encontrado = lista.buscar(n1)

print(f'O valor {n1} está na posição {n1_encontrado} (-1 para não encontrado)')

n2 = 15
n2_encontrado = lista.buscar(n2)
print(f'O valor {n2} está na posição {n2_encontrado} (-1 para não encontrado)')
