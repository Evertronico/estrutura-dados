class Editor:
    
    def __init__(self):
        # pilha de ações realizadas
        self.undo = []
        # pilha de ações desfeitas
        self.redo = []
        
    def adicionar(self,texto):
        # adiciona uma ação na pilha undo
        self.undo.append(texto)
        # ao adiciionar uma nova ação limpa o historico redo
        self.redo.clear()
        # imprime a ação realizada
        print(f"Texto adicionado: {texto}")
        
    def desfazer(self):
        # verifica se existe algun texto
        if len(self.undo) == 0:
            print("Nenhuma ação para desfazer")
            return
        
        # remove do topo do undo
        acao = self.undo.pop()
        
        # envia para a pilha redo
        self.redo.append(acao)
        
    def refazer(self):
        # verifica se existe ação desfeita
        if len(self.redo) == 0:
            print("Nenhuma ação para refazer")
            return
        
        # remove do todo do redo[]
        acao  = self.redo.pop()
        
        # retorna para undo
        self.undo.append(acao)
        
    def exibir(self):
        print("\n------------Estado do editor-------------")
        print("\nAções atuais: ")
        # exibe ação do topo para a base
        for acao in reversed(self.undo):
            print(acao)
        # exibe ações desfeita
        print("\nAções desfeitas: ")
        for acao in reversed(self.redo):
            print(acao)
        
        