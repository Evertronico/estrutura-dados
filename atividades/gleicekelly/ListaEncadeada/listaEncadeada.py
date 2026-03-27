class No:
    #metodo construtor
    def __init__(self, valor):
        #valor do no
        self.valor = valor
        #ponteiro
        self.proximo = None

#classe lista encadeada
class ListaEncadeada:
    def __init__(self):
        #referencia para o primeiro nó, ponteiro para o inicio da lista
        self.head = None
    #metodo para inserir no inicio da lista
    def inserirInicio(self, valor):
        #cria um novo no
        novo = No(valor)
        #o novo nó aponta para o antigo primeiro nó (para o inicio da lista -> head)
        novo.proximo = self.head
        #atualiza o head da lista
        self.head = novo

    #metodo para exibir a lista 
    def exibir(self):
        #aponta para o inicio da lista
        atual = self.head

        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

    def inserirFim(self, valor):
        #cria um novo nó
        novo = No(valor)
        #se a lista estiver vazia, o novo nó é a head da lista
        if self.head is None:
            self.head = novo
            return
        #caso contrario, percorre a lista ate o final
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo

    #funcao para remover item da lista
    def remover(self, valor):
        atual = self.head
        anterior = None

        while atual:
            #verifica se o valor informado foi encontrado
            if atual.valor == valor:
                #se for o primeiro atualiza qual é o head da lista
                self.head = atual.proximo
            else:
                #caso esteja no meio ou no final
                anterior.proximo = atual.proximo
            return
        
        anterior = atual
        atual = atual.proximo
