#  Classe que representa uma pilha
class Pilha:
    def __init__(self):
        # lista interna da pilha
        self.itens = []
        
        # push -> adiciona um item ao topo da pilha
        def push(self, valor):
            self.itens.append(valor)
            
        #  verifica se a pilha esta vazia
        def vazia(self):
            return len(self.itens) == 0
        
        # pop -> remove o item do topo da pilha e o retorna
        def pop(self):
            # verifica se apilha não esta vazia
            if self.vazia():
                print("Pilha vazia")
                return None
            
            return self.itens.pop()
        
        # peek -> retorna o item do topo da pilha sem removê-lo
        def peek(self):
            if self.vazia():
                print("Pilha vazia")
                return None
            
            return self.itens[-1]
        
        # Exibe o conteúdo da pilha
        def exibir(self):
            print("Pilha:", self.itens)