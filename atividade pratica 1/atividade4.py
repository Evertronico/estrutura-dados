class No:
    def __init__ (self,valor):
        self.dado = valor
        self.proximo = None
        
class ListaEncadeada:
    def __init__(self):
        self.head = None
        
    def inserir(self, valor):
        novo = No(valor)
        
        if self.head is None:
            self.head = novo
            return

        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo
        
    def exibir(self):
        atual = self.head
        while atual:
            print(atual.dado)
            atual = atual.proximo
            
    def buscar(self,valor):
        atual = self.head
        while atual is not None:
            if atual.dado == valor:
                print(f"Encontrado : {atual.dado}")
                return
            atual = atual.proximo
        print("Nada foi encontrado")
                
lista = ListaEncadeada()
lista.inserir(1)
lista.inserir("carro")
lista.inserir(5)
lista.buscar("Carroj")
lista.exibir()
           