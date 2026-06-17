# Estrutura: LISTA DUPLAMENTE ENCADEADA
# Usada para o histório de pedidos entregues.


# ---------------- CLASSE NÓ DUPLO ----------------
class NoDuplo:
    def __init__(self, pedido):
        self.pedido = pedido     
        self.proximo = None      
        self.anterior = None      


class HistoricoPedidos:
    def __init__(self):
        self.head = None          
        self.tail = None          
        self.atual = None         

    # Adiciona um pedido entregue no final do histórico
    def adicionar(self, pedido):
        novo = NoDuplo(pedido)

        # Histórico vazio: novo é o primeiro e o último
        if self.head is None:
            self.head = self.tail = novo
            self.atual = novo
            return

        # Conecta o novo nó após o último (ligação dupla)
        self.tail.proximo = novo
        novo.anterior = self.tail
        self.tail = novo

    # NAVEGAÇÃO PARA FRENTE
    # Move o cursor para o próximo pedido do histórico.
    def avancar(self):
        if self.atual is None:
            print("Histórico vazio.")
            return None
        if self.atual.proximo is None:
            print("Você já está no pedido mais recente.")
            return self.atual.pedido
        self.atual = self.atual.proximo
        return self.atual.pedido

    # NAVEGAÇÃO PARA TRÁS 
    # Move o cursor para o pedido anterior do histórico.
    def voltar(self):
        if self.atual is None:
            print("Histórico vazio.")
            return None
        if self.atual.anterior is None:
            print("Você já está no pedido mais antigo.")
            return self.atual.pedido
        self.atual = self.atual.anterior
        return self.atual.pedido

    # Retorna o pedido onde o cursor está posicionado
    def atual_pedido(self):
        if self.atual is None:
            return None
        return self.atual.pedido

    # Exibe o histórico do mais antigo para o mais recente (frente)
    def exibir_frente(self):
        if self.head is None:
            print("Histórico vazio.")
            return
        print("Histórico (mais antigo -> mais recente)")
        no = self.head
        while no:
            print(no.pedido)
            no = no.proximo

    # Exibe o histórico do mais recente para o mais antigo (trás)
    def exibir_tras(self):
        if self.tail is None:
            print("Histórico vazio.")
            return
        print("Histórico (mais recente -> mais antigo)")
        no = self.tail
        while no:
            print(no.pedido)
            no = no.anterior
