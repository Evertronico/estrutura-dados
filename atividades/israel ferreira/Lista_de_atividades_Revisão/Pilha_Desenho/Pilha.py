from Acao import Acao

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, acao):
        self.itens.append(acao)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def mostrar_ultima_acao(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None

    def exibir_historico(self):
        if self.esta_vazia():
            print("Histórico de ações vazio.")
            return
        print("Histórico de Ações (da mais antiga para a mais recente):")
        for i, acao in enumerate(self.itens):
            print(f"{i+1}. {acao}")
