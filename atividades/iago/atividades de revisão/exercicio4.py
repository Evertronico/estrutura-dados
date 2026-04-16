# Classe do nó (estrutura básica)
class No:
    def __init__(self, dado):
        self.dado = dado # armazena informação
        self.proximo = None # ponteiro

# Classe da lista encadeada
class ListaEncadeada:
    def __init__(self):
        self.head = None # início da lista

    # Inserção no final (simula histórico)
    def inserir(self, valor):
        novo = No(valor) # cria nó
        # caso lista vazia
        if self.head is None:
            self.head = novo
            return
        # percorre até o final
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo # conecta novo nó

    # Exibir lista (percurso)
    def exibir(self):
        atual = self.head
        while atual:
            print(atual.dado)
            atual = atual.proximo

# uso do sistema
lista = ListaEncadeada()
lista.inserir("google.com")
lista.inserir("youtube.com")
lista.inserir("github.com")
lista.exibir()