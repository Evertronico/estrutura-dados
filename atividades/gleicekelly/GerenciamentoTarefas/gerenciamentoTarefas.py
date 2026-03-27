from datetime import datetime

class No:
    def __init__(self, descricao, prioridade, dataHora):
        self.descricao = descricao
        self.prioridade = prioridade
        self.dataHora = dataHora
        self.proximo = None

class GerenciamentoTarefas:
    def __init__(self):
        self.head = None

    def gravarTarefa(self, descricao, prioridade):
        dataHora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        novo = No(descricao, prioridade, dataHora)

        if self.head is None:
            self.head = novo
            return
        
        #atual recebe o head para começar
        atual = self.head
        #enquanto tiver um proximo, entra no loop
        while atual.proximo:
            #atual vai receber o proximo valor inserido
            atual = atual.proximo
            #valor novo vai receber o proximo da lista : novo = No(descricao, dataHora)
        atual.proximo = novo

    def exibir(self):
        if self.head is None:
            print("Nenhuma tarefa encontrada.")
            return

        atual = self.head

        while atual:
            print(f"Tarefa: {atual.descricao} , {atual.prioridade} | Data e hora da criação: {atual.dataHora}")
            atual = atual.proximo

    def remover(self, descricao):
        atual = self.head
        anterior = None

        while atual:
            if atual.descricao == descricao:
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                print("Tarefa removida com sucesso!")
                return
            
            anterior = atual
            atual = atual.proximo

        print("Tarefa não encontrada.")