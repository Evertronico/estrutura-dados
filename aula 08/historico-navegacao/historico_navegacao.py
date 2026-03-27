from datetime import datetime

class No:
    def __init__(self, site, data_hora):
        self.site = site
        self.data_hora = data_hora
        self.proximo = None


class HistoricoNavegacao:

    def __init__(self):
        self.head = None

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

    def ler(self):
        atual = self.head

        while atual:
            print(f"Site: {atual.site} | {atual.data_hora}")
            atual = atual.proximo

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