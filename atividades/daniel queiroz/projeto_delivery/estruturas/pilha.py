# Estrutura: PILHA 
# Usada para o HISTÓRICO DE STATUS de cada pedido.


class Pilha:
    def __init__(self):
        # Lista interna onde o final representa o TOPO da pilha
        self.itens = []

    # Adiciona um elemento no topo da pilha complexidade O(1).
    def empilhar(self, valor):
        self.itens.append(valor)

    # Remove e retorna o elemento do topo complexidade O(1).
    def desempilhar(self):
        if self.esta_vazia():
            return None
        return self.itens.pop()

    # Retorna o elemento do topo SEM removê-lo complexidade O(1).
    def topo(self):
        if self.esta_vazia():
            return None
        return self.itens[-1]

    # Verifica se a pilha está vazia
    def esta_vazia(self):
        return len(self.itens) == 0

    # Quantidade de elementos na pilha
    def tamanho(self):
        return len(self.itens)
