class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.vazia():
            return self.itens.pop()
        return None

    def vazia(self):
        return len(self.itens) == 0

    def __str__(self):
        return str(self.itens)


class Editor:
    def __init__(self):
        self.pilhaUndo = Pilha()
        self.pilhaRedo = Pilha()

    def nova_acao(self, acao):
        self.pilhaUndo.push(acao)
        self.pilhaRedo.itens.clear()  # limpa redo

    def desfazer(self):
        if not self.pilhaUndo.vazia():
            acao = self.pilhaUndo.pop()
            self.pilhaRedo.push(acao)
            print("Desfeito:", acao)
        else:
            print("Nada para desfazer.")

    def refazer(self):
        if not self.pilhaRedo.vazia():
            acao = self.pilhaRedo.pop()
            self.pilhaUndo.push(acao)
            print("Refeito:", acao)
        else:
            print("Nada para refazer.")

    def mostrar_historico(self):
        print("\n--- Histórico ---")
        print("Undo:", self.pilhaUndo)
        print("Redo:", self.pilhaRedo)
        print("-----------------\n")
