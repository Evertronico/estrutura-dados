
# Estrutura: FILA 


class Fila:
    def __init__(self):
        
        self.itens = []

    # Adiciona um elemento no FINAL da fila. O(1).
    def enfileirar(self, valor):
        self.itens.append(valor)

    # Remove e retorna o elemento do INÍCIO da fila. O(n) por causa
    # do deslocamento dos elementos 
    def desenfileirar(self):
        if self.esta_vazia():
            return None
        return self.itens.pop(0)

    # Retorna o primeiro elemento SEM removê-lo.
    def primeiro(self):
        if self.esta_vazia():
            return None
        return self.itens[0]

    # Verifica se a fila está vazia
    def esta_vazia(self):
        return len(self.itens) == 0

    # Quantidade de elementos na fila
    def tamanho(self):
        return len(self.itens)

    # Exibe todos os pedidos aguardando na fila
    def exibir(self):
        if self.esta_vazia():
            print("Fila de preparo vazia.")
            return
        print("----- Fila de preparo (primeiro -> último) -----")
        for valor in self.itens:
            print(valor)
