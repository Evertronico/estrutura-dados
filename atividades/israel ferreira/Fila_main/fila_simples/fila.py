class Fila:
    def __init__(self):
        # cria estrutura principal da fila
        self.dados = []

    #  insere o elemento no fianal da fila
    def entrar(self, valor):
        # adiciona o valor no fianl da fila
        self.dados.append(valor)
        # imprime o valor inserido
        print(f"Valor {valor} entrou na fila.")
    
    # remove o elementpo do inicio da fila
    def sair(self):
        # verifica se a fila esta vazia
        if len(self.dados) == 0:
            print("Fila vazia.")
            return
        # remove o primeiro elemento da fila
        removido = self.dados.pop(0)
        # imprime o valor removido
        print(f"Valor {removido} saiu da fila.")
        
    # exibe a fila
    def exibir(self):
         # verifica se a fila esta vazia
        if len(self.dados) == 0:
            print("Fila vazia.")
            return
        # exibe os elementos da fila
        print("Fila:", self.dados)