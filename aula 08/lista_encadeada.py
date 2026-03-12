class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:

    def __init__(self):
        # referência para o primeiro nó
        self.head = None

    def inserir_inicio(self, valor):
        novo = No(valor)

        # o novo nó aponta para o antigo primeiro nó
        novo.proximo = self.head

        # atualiza a cabeça da lista
        self.head = novo

    def exibir(self):

        atual = self.head

        while atual:
            print(atual.dado)
            atual = atual.proximo

    def inserir_final(self, valor):

        novo = No(valor)

        if self.head is None:
            self.head = novo
            return

        atual = self.head

        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo
    
    def remover(self, valor):

        atual = self.head
        anterior = None

        while atual:

            if atual.dado == valor:

                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                return

            anterior = atual
            atual = atual.proximo