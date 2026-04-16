class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, valor):
        novo = No(valor)
        if self.head is None:
            self.head = novo
            return
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo

    # remoção
    def remover(self, valor):
        atual = self.head # começa no início
        anterior = None # não há anterior inicialmente
        while atual:
            # encontrou o valor
            if atual.dado == valor:
                # remove o primeiro
                if anterior is None:
                    self.head = atual.proximo
                else:
                    # remove do meio/fim
                    anterior.proximo = atual.proximo
                return
            # avança ponteiros
            anterior = atual
            atual = atual.proximo

    def exibir(self):
        atual = self.head
        while atual:
            print(atual.dado)
            atual = atual.proximo

# uso
lista = ListaEncadeada()
lista.inserir(10)
lista.inserir(20)
lista.inserir(30)
lista.remover(20)
lista.exibir()