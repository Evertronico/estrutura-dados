class Sanduiche:
    def __init__(self):
        self.ingredientes = []

    def pilha_vazia(self):
        return len(self.ingredientes) == 0

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
        print(f"Ingrediente adicionado: {ingrediente}")

    def remover_ingrediente(self):
        if self.pilha_vazia():
            print("Aviso: O sanduíche não tem ingredientes para remover.")
            return None
        
        ingrediente_removido = self.ingredientes.pop()
        print(f"Ingrediente removido: {ingrediente_removido}")
        return ingrediente_removido

    def exibir_montagem(self):
        if self.pilha_vazia():
            print("Status: O prato está vazio.")
        else:
            print("Montagem Atual (do topo para a base):")
            for ingrediente in reversed(self.ingredientes):
                print(f"  -> {ingrediente}")

if __name__ == "__main__":
    print("SISTEMA DE MONTAGEM DE SANDUÍCHES\n")
    
    pedido = Sanduiche()
    
    print("--- Iniciando Pedido Personalizado ---")
    pedido.adicionar_ingrediente("Pão Australiano (Base)")
    pedido.adicionar_ingrediente("Hambúrguer Artesanal")
    pedido.adicionar_ingrediente("Queijo Cheddar")
    pedido.adicionar_ingrediente("Bacon")
    pedido.adicionar_ingrediente("Cebola Caramelizada")
    pedido.adicionar_ingrediente("Molho Barbecue")
    pedido.adicionar_ingrediente("Pão Australiano (Topo)")
    
    print("\n--- Verificando Montagem ---")
    pedido.exibir_montagem()
    
    print("\n--- Alteração Solicitada pelo Cliente ---")
    print("Cliente: 'Mudei de ideia, tire o pão de cima e o molho barbecue, por favor!'")
    pedido.remover_ingrediente() 
    pedido.remover_ingrediente() 
    
    print("\n--- Retomando a Montagem ---")
    pedido.adicionar_ingrediente("Molho Especial")
    pedido.adicionar_ingrediente("Pão Australiano (Topo)")
    
    print("\n--- Montagem Final ---")
    pedido.exibir_montagem()
    print("\nPedido finalizado e pronto para entrega.")