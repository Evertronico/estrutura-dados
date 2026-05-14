class editor:
    
    def __init__(self):
        self.undo = []
        
    def adicionar(self, texto):
        # salva uma ação 
        self.undo.append(texto)

    def desfazer(self):
        if len(self.undo) == 0:
            print("Nada para desfazer.")
            return
        
        removido = self.undo.pop()
        print(f"Desfeito: {removido}")
        
    def mostrar(self):
        for texto in self.undo:
            print(texto)