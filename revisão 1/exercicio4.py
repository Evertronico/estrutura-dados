# classe Nó (estrutura básica)
class No:
    def __init__(self, url):
        self.url = url
        self.ponteiro = None

# classe da lista encadeada
class ListaEncadeada:
    def __init__(self):
        self.head = None

    # inserção no final simula o histórico de navegação
    def inserir(self, url):
        # cria um novo nó com a URL informada
        novo = No(url) 

        # caso a lista esteja vazia
        if self.head is None:
            self.head = novo
        else:
            # percorre a lista até o final
            atual = self.head
            while atual.ponteiro is not None:
                atual = atual.ponteiro
            # insere o novo nó no final da lista
            atual.ponteiro = novo

    
    # exibir lista (todo o percurso de navegação)
    def exibir(self):
        atual = self.head
        while atual is not None:
            print(atual.url)
            atual = atual.ponteiro

# cria uma lista encadeada
lista = ListaEncadeada()

lista.inserir("www.google.com")
lista.inserir("www.facebook.com")
lista.inserir("www.youtube.com")

lista.exibir()