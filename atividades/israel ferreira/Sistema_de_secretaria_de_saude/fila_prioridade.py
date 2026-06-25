class FilaPrioridade:
    
    # construtor
    def __init__(self, solicitacoes):
        # cria uma lista com as solicitações
        self.fila = solicitacoes
        # aplicar o método de ordenação da lista
        self.ordernar()
        
    def ordernar(self):
        tamanho = len(self.fila)
        
        for i in range(tamanho):
            for j in range(tamanho - i - 1):
                if (self.fila[j].prioridade() < self.fila[j+1].prioridade()):
                    temp = self.fila[j]
                    self.fila[j] = self.fila[j+1]
                    self.fila[j+1] = temp
                    
    def exibir(self):
        if len(self.fila) == 0:
            print("\nFila Vazia!\n")
            return
        print("\n========= FILA ATUAL ===========\n")
        posicao = 1
        for item in self.fila:
            print(f"{posicao}° -> {item}")
            posicao += 1
            
    def atender(self):
        if len(self.fila) == 0:
            print("\nFila Vazia!\n")
            return None
        paciente = self.fila[0]
        nova_fila = []
        
        for i in range(1, len(self.fila)):
            nova_fila.append(self.fila[i])
            
        self.fila = nova_fila
        return paciente
            