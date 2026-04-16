class ListaSeq:
    def __init__(self):
        self.lista = [None] * 5
        self.tamanho = 0

    def inserir(self, posicao, numero):
        if 0 <= posicao <= self.tamanho:
            for i in range(self.tamanho, posicao, -1):
                self.lista[i] = self.lista[i-1]
            self.lista[posicao] = numero
            self.tamanho += 1
        else:
            print("Posição inválida")

        
    def remover(self, numero):
        for i in range(self.tamanho):
            if self.lista[i] == numero:
                for j in range(i, self.tamanho - 1):
                    self.lista[j] = self.lista[j + 1]
                self.lista[self.tamanho - 1] = None
                self.tamanho -= 1
                return
            print("Número não encontrado")

    def buscar(self, numero):
        for i in range(self.tamanho):
            if self.lista[i] == numero:
                return True
            return False
        

    def exibir(self):
        print("Elementos: ", self.lista[:self.tamanho])


lista = ListaSeq()
lista.inserir(0, 10)
lista.inserir(1, 23)
lista.inserir(2, 512)
lista.inserir(3, 111112)
lista.inserir(4, 19)
lista.exibir()