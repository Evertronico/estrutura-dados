from no import No;

class ListaDupla:

    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_inicio(self, valor):
        novo = No(valor)

        # lista vazia
        if self.head is None:
            self.head = self.tail = novo
            return

        # conecta novo ao antigo primeiro
        novo.proximo = self.head
        self.head.anterior = novo

        # atualiza head
        self.head = novo

    def inserir_final(self, valor):
        novo = No(valor)

        # lista vazia
        if self.tail is None:
            self.head = self.tail = novo
            return

        # conecta no final
        self.tail.proximo = novo
        novo.anterior = self.tail

        # atualiza tail
        self.tail = novo

    def remover(self, valor):
        atual = self.head

        while atual:

            if atual.dado == valor:

                # remoção no início
                if atual.anterior is None:
                    self.head = atual.proximo
                    if self.head:
                        self.head.anterior = None

                # remoção no final
                elif atual.proximo is None:
                    self.tail = atual.anterior
                    self.tail.proximo = None

                # remoção no meio
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior

                return

            atual = atual.proximo
    
    def exibir(self):
        atual = self.head

        while atual:
            print(atual.dado)
            atual = atual.proximo