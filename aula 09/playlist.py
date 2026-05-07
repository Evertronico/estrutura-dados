# Classe do nó
class No:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None
        self.anterior = None


# Classe da playlist (lista duplamente encadeada)
class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.atual = None

    # adiciona música no final
    def adicionar(self, musica):
        novo = No(musica)

        if self.head is None:
            self.head = self.tail = self.atual = novo
            return

        self.tail.proximo = novo
        novo.anterior = self.tail
        self.tail = novo

    # exibe música atual
    def tocar(self):
        if self.atual:
            print("Tocando:", self.atual.musica)

    # avança para próxima música
    def avancar(self):
        if self.atual and self.atual.proximo:
            print("Avançando...")
            self.atual = self.atual.proximo
            self.tocar()
        else:
            print("Não há próxima música.")

    # volta para música anterior
    def voltar(self):
        if self.atual and self.atual.anterior:
            print("Voltando...")
            self.atual = self.atual.anterior
            self.tocar()
        else:
            print("Não há música anterior.")

playlist = Playlist()

# adicionando músicas
playlist.adicionar("Música A")
playlist.adicionar("Música B")
playlist.adicionar("Música C")

# fluxo 
playlist.tocar()
playlist.avancar()
playlist.voltar()