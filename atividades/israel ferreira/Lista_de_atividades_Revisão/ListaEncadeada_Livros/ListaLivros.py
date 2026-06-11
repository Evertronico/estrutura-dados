from estrutura_No import No
from Livro import Livro

class ListaLivros:
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def inserir_final(self, livro):
        novo_no = No(livro)
        if self.head is None:
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def buscar_livro(self, titulo):
        atual = self.head
        while atual:
            if atual.dado.titulo == titulo:
                return atual.dado
            atual = atual.proximo
        return None

    def remover_livro(self, titulo):
        atual = self.head
        anterior = None

        while atual:
            if atual.dado.titulo == titulo:
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def exibir_livros(self):
        if self.head is None:
            print("A lista de livros está vazia.")
            return
        atual = self.head
        while atual:
            print(atual.dado)
            atual = atual.proximo

    def quantidade_livros(self):
        return self.tamanho
