class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir_final(self, valor):
        novo_no = Node(valor)
        if not self.head:
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def buscar(self, valor):
        atual = self.head
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def exibir(self):
        atual = self.head
        saida = ""
        while atual:
            saida += f"{atual.valor} -> "
            atual = atual.proximo
        print(saida + "None")

# Demonstração no programa principal
lista = ListaEncadeada()
lista.inserir_final(10)
lista.inserir_final(20)
lista.inserir_final(30)
lista.exibir()
print(f"Busca pelo 20: {lista.buscar(20)}")
print(f"Busca pelo 50: {lista.buscar(50)}")