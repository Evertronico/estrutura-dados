"""
    Exercício 2 – Sistema de Investigação Criminal
    Implemente um sistema de investigação onde evidências coletadas são armazenadas em uma pilha para análise reversa dos acontecimentos. O investigador deve conseguir revisar as últimas evidências coletadas primeiro.

    Requisitos:
        Implementar classe Investigacao

        Registrar evidências

        Analisar última evidência coletada

        Exibir histórico de evidências

        Validar estrutura vazia

        Simular cenário de perícia criminal
"""
class Investigacao:
    
    def __init__(self):

        self.evidencias = []
        
    def registrar(self, evidencia):

        self.evidencias.append(evidencia)
        print(f"Evidência registrada: {evidencia}")
        
    def analisar(self):

        if len(self.evidencias) == 0:
            print("Nenhuma evidência para analisar (pilha vazia)")
            return
        
        evidencia = self.evidencias.pop()
        print(f"Analisando evidência: {evidencia}")
        
    def exibir(self):
        print("\n------------ Histórico de Evidências ------------")
        if len(self.evidencias) == 0:
            print("Nenhuma evidência registrada!")
        else:
            print("Evidências (última coletada no topo):")
            for envest in reversed(self.evidencias):
                print(f"- {envest}")
        print("-------------------------------------------------")

