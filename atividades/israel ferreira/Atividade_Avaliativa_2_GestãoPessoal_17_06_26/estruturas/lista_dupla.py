class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None
        self.atual = None

    def inserir(self, dado):
        novo_no = NoDuplo(dado)
        if not self.head:
            self.head = novo_no
            self.tail = novo_no
            self.atual = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
            self.tail = novo_no

    def navegar_proximo(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            return self.atual.dado
        return None

    def navegar_anterior(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            return self.atual.dado
        return None

    def obter_atual(self):
        return self.atual.dado if self.atual else None
