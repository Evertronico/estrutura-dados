from Cliente import Cliente

class Fila:
    def __init__(self):
        self.itens = []

    def adicionar_cliente(self, cliente):
        self.itens.append(cliente)
        print(f"Cliente {cliente.nome} adicionado à fila.")

    def atender_cliente(self):
        if not self.esta_vazia():
            cliente_atendido = self.itens.pop(0)
            print(f"Cliente {cliente_atendido.nome} atendido.")
            return cliente_atendido
        print("Fila vazia. Nenhum cliente para atender.")
        return None

    def exibir_fila_completa(self):
        if self.esta_vazia():
            print("Fila de clientes vazia.")
            return
        print("Fila de Clientes:")
        for i, cliente in enumerate(self.itens):
            print(f"  {i+1}. {cliente}")

    def quantidade_clientes_aguardando(self):
        print(f"Quantidade de clientes aguardando: {len(self.itens)}")
        return len(self.itens)

    def exibir_proximo_cliente(self):
        if not self.esta_vazia():
            print(f"Próximo cliente a ser atendido: {self.itens[0].nome}")
            return self.itens[0]
        print("Fila vazia. Nenhum próximo cliente.")
        return None

    def esta_vazia(self):
        return len(self.itens) == 0
