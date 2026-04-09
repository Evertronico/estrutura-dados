from datetime import datetime

class No:
    # método construtor espera url e data e hora
    def __init__(self, site, data_hora):
        self.site = site
        self.data_hora = data_hora
        self.proximo = None

class HistoricoNavegacao:

    # método construtor
    def __init__(self):
        self.head = None

    # método visitar
    def visitar(self, site):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        novo = No(site, data_hora)

        if self.head is None:
            self.head = novo
            return

        atual = self.head
        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo

    # método ler
    def ler(self):
        atual = self.head

        while atual:
            print(f"Site: {atual.site} | Data e hora {atual.data_hora}")
            atual = atual.proximo

    # método apagar
    def apagar(self, site):
        atual = self.head
        anterior = None

        while atual:
            if atual.site == site:
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return

            anterior = atual
            atual = atual.proximo