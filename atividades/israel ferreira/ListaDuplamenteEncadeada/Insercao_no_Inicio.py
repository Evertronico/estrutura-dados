from No import No;

class ListaDupla:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def inserir_inicio(self, dado):
        novo = No(dado)
        
        # Lista vazia
        if self.head is None:
            self.head = self.tail = novo
            return
        
        # Conecta novo ao antigo primeiro
        novo.proximo = self.head
        self.tail.anterior = novo
        
        # Atualiza a lista.
        self.head = novo
    
    
    def inserir_final(self, dado):
        novo = No(dado)
        
        # Lista vazia
        if self.head is None:
            self.head = self.tail = novo
            return
        
        # Conecta final
        self.tail.proximo = novo
        novo.anterior = self.tail
        
        # Atualiza a lista.
        self.tail = novo
        
    def remover(self, valor):
        atual = No(valor)
        
        #enquanto ouver
        while atual:
        
            if atual.dado == valor:
                
                # Remoção no inicio
                if atual.anterior is None:
                    self.head = atual.proximo
                    if self.head:
                        self.head.anterior = None
                
                # Remoção Final
                elif atual.proximo is None:
                    self.tail = atual.anterior
                    self.tail.proximo = None
                
                # Remoção Meio
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterio  = atual.anterior
                    
                return
            
            atual = atual.proximo
            
    
    def exibir(self):
        atual = self.head
        
        while atual:
            print(atual.dado)
            atual = atual.proximo
                
            
            
        
        
        
        