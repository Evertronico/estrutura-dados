from estrutura_No import No
from Tarefa import Tarefa

class ListaTarefas:
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def inserir_final(self, tarefa):
        novo_no = No(tarefa)
        if self.head is None:
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def buscar_tarefa(self, descricao):
        atual = self.head
        while atual:
            if atual.dado.descricao == descricao:
                return atual.dado
            atual = atual.proximo
        return None

    def remover_tarefa(self, descricao):
        atual = self.head
        anterior = None

        while atual:
            if atual.dado.descricao == descricao:
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def exibir_tarefas_pendentes(self):
        if self.head is None:
            print("Não há tarefas pendentes.")
            return
        atual = self.head
        print("Tarefas Pendentes:")
        while atual:
            print(atual.dado)
            atual = atual.proximo

    def quantidade_tarefas(self):
        return self.tamanho
