# Requisito 1: Estrutura de nó com múltiplos atributos
class Tarefa:
    def __init__(self, descricao, prioridade, data):
        self.descricao = descricao
        self.prioridade = prioridade
        self.data = data
        self.proximo = None  # Ponteiro para o próximo nó

# Requisito 2: Classe de lista encadeada
class ListaTarefasEncadeada:
    def __init__(self):
        self.cabeca = None

    # Requisito 3: Implementar inserir (no final)
    def inserir_final(self, descricao, prioridade, data):
        novo_no = Tarefa(descricao, prioridade, data)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    # Requisito 3: Implementar remover por descrição
    def remover_por_descricao(self, desc_alvo):
        atual = self.cabeca
        anterior = None
        
        while atual:
            if atual.descricao.lower() == desc_alvo.lower():
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    # Requisito 3: Implementar exibir
    def exibir_lista(self):
        if not self.cabeca:
            print("\n[!] A lista de tarefas está vazia.")
            return
        
        print("\n--- TAREFAS CADASTRADAS ---")
        atual = self.cabeca
        while atual:
            print(f"DESCRIÇÃO: {atual.descricao} | PRIORIDADE: {atual.prioridade} | DATA: {atual.data}")
            atual = atual.proximo