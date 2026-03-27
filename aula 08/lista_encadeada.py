# Define a classe No (elemento da lista encadeada)
class No:
    def __init__(self, dado):
        # Armazena o valor dentro do nó
        self.dado = dado
        
        # Ponteiro para o próximo nó (inicialmente não aponta para ninguém)
        self.proximo = None


# Define a estrutura da lista encadeada
class ListaEncadeada:

    def __init__(self):
        # head é a referência para o primeiro nó da lista
        # Se for None, significa que a lista está vazia
        self.head = None

    # Método para inserir um elemento no início da lista
    def inserir_inicio(self, valor):

        # Cria um novo nó com o valor informado
        novo = No(valor)

        # O novo nó passa a apontar para o antigo primeiro nó
        # (ou None, caso a lista esteja vazia)
        novo.proximo = self.head

        # Atualiza o head para o novo nó
        # Agora ele é o primeiro elemento da lista
        self.head = novo

    # Método para exibir todos os elementos da lista
    def exibir(self):

        # Começa a percorrer a lista a partir do primeiro nó
        atual = self.head

        # Enquanto existir um nó válido (diferente de None)
        while atual:

            # Exibe o valor armazenado no nó atual
            print(atual.dado)

            # Avança para o próximo nó da lista
            atual = atual.proximo

    # Método para inserir um elemento no final da lista
    def inserir_final(self, valor):
        # Cria um novo nó com o valor informado
        novo = No(valor)

        # Caso a lista esteja vazia
        if self.head is None:
            # O novo nó se torna o primeiro elemento
            self.head = novo
            # Encerra a função
            return

        # Começa a percorrer a lista a partir do início
        atual = self.head

        # Enquanto o nó atual tiver um próximo elemento (ou seja, ainda não chegou no último)
        while atual.proximo:
            # Avança para o próximo nó
            atual = atual.proximo

        # Quando sair do loop, atual será o último nó Faz ele apontar para o novo nó
        atual.proximo = novo

    # Método para remover um elemento da lista
    def remover(self, valor):
        # Ponteiro para o nó atual (começa no início)
        atual = self.head
        # Ponteiro para o nó anterior (inicialmente não existe)
        anterior = None

        # Percorre a lista enquanto houver nós
        while atual:
            # Verifica se encontrou o valor desejado
            if atual.dado == valor:
                # Caso o elemento a ser removido seja o primeiro
                if anterior is None:
                    # O head passa a apontar para o próximo nó (remove o primeiro elemento)
                    self.head = atual.proximo
                else:
                    # Caso seja um nó do meio ou final O anterior "pula" o atual
                    anterior.proximo = atual.proximo

                # Encerra a função após remover
                return

            # Atualiza o ponteiro anterior para o nó atual
            anterior = atual
            # Avança para o próximo nó
            atual = atual.proximo