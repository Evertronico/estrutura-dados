from NoDuplo import NoDuplo
from Versao import Versao

class HistoricoEdicao:
    def __init__(self):
        self.head = None
        self.tail = None
        self.atual = None  # Ponteiro para a versão atual

    def adicionar_versao(self, descricao_alteracao):
        nova_versao = Versao(descricao_alteracao)
        novo_no = NoDuplo(nova_versao)

        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            # Se houver versões à frente da atual, elas são descartadas
            if self.atual and self.atual.proximo:
                self.atual.proximo = None
                self.tail = self.atual

            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
            self.tail = novo_no
        self.atual = novo_no

    def avancar_versao(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            return True
        return False

    def retornar_versao(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            return True
        return False

    def exibir_versao_atual(self):
        if self.atual:
            return f"Versão Atual: {self.atual.dado.descricao}"
        return "Nenhuma versão no histórico."

    def exibir_historico(self):
        if self.head is None:
            print("Histórico de versões vazio.")
            return
        temp = self.head
        historico = []
        while temp:
            prefixo = "* " if temp == self.atual else "  "
            historico.append(f"{prefixo}{temp.dado.descricao}")
            temp = temp.proximo
        print("Histórico de Versões:")
        for item in historico:
            print(item)

