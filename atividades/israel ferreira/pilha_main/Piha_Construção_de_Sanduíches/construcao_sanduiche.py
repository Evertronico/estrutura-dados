"""
    Exercício 3 – Sistema de Construção de Sanduíches
    Implemente um sistema para montagem de sanduíches personalizados utilizando pilha. Cada ingrediente adicionado deve ser empilhado e a remoção deve ocorrer na ordem inversa da montagem.

    Requisitos:
        Implementar classe Sanduiche

        Adicionar ingredientes

        Remover último ingrediente

        Exibir montagem atual

        Validar pilha vazia

        Simular pedidos personalizados de clientes
"""
class Sanduiche:
    
    def __init__(self):
        self.ingredientes = []
        
    def adicionar(self, ingrediente):

        self.ingredientes.append(ingrediente)
        print(f"Ingrediente adicionado: {ingrediente}")
        
    def remover(self):
        if len(self.ingredientes) == 0:
            
            print("Nenhum ingrediente para remover (pilha vazia)")
            return
        
        ingrediente = self.ingredientes.pop()
        print(f"Ingrediente removido: {ingrediente}")
        
    def exibir(self):
        print("\n------------ Montagem do Sanduíche ------------")
        if len(self.ingredientes) == 0:
            print("Sanduíche vazio!")
        else:
            print("Ingredientes (do topo para a base):")
            for ing in reversed(self.ingredientes):
                print(f"- {ing}")
        print("-----------------------------------------------")

