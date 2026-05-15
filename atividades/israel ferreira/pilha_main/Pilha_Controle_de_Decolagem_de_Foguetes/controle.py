"""
    Exercício 1 – Sistema de Controle de Decolagem de Foguetes
    Implemente um sistema de controle de etapas de lançamento de um foguete utilizando pilha. Cada etapa do lançamento deve ser armazenada em ordem de execução, permitindo abortar o lançamento desfazendo as etapas na ordem inversa.

    Requisitos:
        Implementar classe ControleLancamento

        Registrar etapas do lançamento

        Implementar operação de abortar lançamento

        Exibir etapas restantes

        Validar pilha vazia

        Simular sequência real de lançamento espacial
"""

class ControleLancamento:
    
    def __init__(self):
        self.undo = []
        self.redo = []
        
    def adicionar(self, etapa):

        self.undo.append(etapa)

        self.redo.clear()
        print(f"Etapa registrada: {etapa}")
        
    def desfazer(self):

        if len(self.undo) == 0:
            print("Nenhuma etapa para desfazer (pilha vazia)")
            return
        

        etapa = self.undo.pop()

        self.redo.append(etapa)
        print(f"Etapa abortada: {etapa}")
        
    def refazer(self):

        if len(self.redo) == 0:
            print("Nenhuma etapa para refazer")
            return
        
        etapa  = self.redo.pop()

        self.undo.append(etapa)
        print(f"Etapa retomada: {etapa}")
        
    def exibir(self):
        print("\n------------ Estado do Lançamento ------------")
        print("Etapas atuais (ativas):")
        for etapa in reversed(self.undo):
            print(f"- {etapa}")
        print("\nEtapas abortadas (desfeitas):")
        for etapa in reversed(self.redo):
            print(f"- {etapa}")
        print("----------------------------------------------")


