from no import No

# Classe do Cache LRU
class CacheLRU:

    def __init__(self, capacidade):
        self.capacidade = capacidade

        # Estrutura auxiliar para acesso rápido O(1)
        self.cache = {}

        # Ponteiros da lista
        self.head = None  # mais recente
        self.tail = None  # menos recente

    def _adicionar_no_inicio(self, no):

        no.proximo = self.head
        no.anterior = None

        if self.head:
            self.head.anterior = no

        self.head = no

        if self.tail is None:
            self.tail = no

    def _remover_no(self, no):

        if no.anterior:
            no.anterior.proximo = no.proximo
        else:
            self.head = no.proximo

        if no.proximo:
            no.proximo.anterior = no.anterior
        else:
            self.tail = no.anterior

    def _mover_para_inicio(self, no):
        self._remover_no(no)
        self._adicionar_no_inicio(no)

    def get(self, chave):

        if chave not in self.cache:
            print("Chave não encontrada")
            return None

        no = self.cache[chave]

        # move para mais recente
        self._mover_para_inicio(no)

        return no.valor

    def put(self, chave, valor):

        # se já existe, atualiza
        if chave in self.cache:
            no = self.cache[chave]
            no.valor = valor
            self._mover_para_inicio(no)
            return

        # cria novo nó
        novo = No(chave, valor)

        # adiciona no início
        self._adicionar_no_inicio(novo)

        # adiciona no dicionário
        self.cache[chave] = novo

        # verifica capacidade
        if len(self.cache) > self.capacidade:

            # remove o menos usado (tail)
            chave_removida = self.tail.chave
            self._remover_no(self.tail)

            del self.cache[chave_removida]

    def exibir(self):

        atual = self.head

        print("Cache (mais recente -> menos recente):")

        while atual:
            print(f"{atual.chave}: {atual.valor}")
            atual = atual.proximo