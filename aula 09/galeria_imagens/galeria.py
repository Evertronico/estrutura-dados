from no import No

class Galeria:

    def __init__(self):
        self.head = None
        self.tail = None
        self.atual = None

    def adicionar(self, imagem):
        novo = No(imagem)

        if self.head is None:
            self.head = self.tail = self.atual = novo
            return

        self.tail.proximo = novo
        novo.anterior = self.tail
        self.tail = novo

    def proxima(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            print("Imagem atual:", self.atual.imagem)

    def anterior(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            print("Imagem atual:", self.atual.imagem)

    def exibir_atual(self):
        if self.atual:
            print("Imagem atual:", self.atual.imagem)