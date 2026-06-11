from Pedido import Pedido

class Fila:
    def __init__(self):
        self.itens = []

    def registrar_pedido(self, pedido):
        self.itens.append(pedido)
        print(f"Pedido {pedido.id_pedido} registrado: {pedido.descricao}")

    def processar_proximo_pedido(self):
        if not self.esta_vazia():
            pedido_processado = self.itens.pop(0)
            print(f"Pedido {pedido_processado.id_pedido} processado: {pedido_processado.descricao}")
            return pedido_processado
        print("Fila de pedidos vazia. Nenhum pedido para processar.")
        return None

    def exibir_pedidos_pendentes(self):
        if self.esta_vazia():
            print("Não há pedidos pendentes.")
            return
        print("Pedidos Pendentes (ordem FIFO):")
        for i, pedido in enumerate(self.itens):
            print(f"  {i+1}. {pedido}")

    def consultar_proximo_pedido(self):
        if not self.esta_vazia():
            print(f"Próximo pedido a ser processado: {self.itens[0].id_pedido} - {self.itens[0].descricao}")
            return self.itens[0]
        print("Fila de pedidos vazia. Nenhum próximo pedido.")
        return None

    def quantidade_pedidos_aguardando(self):
        print(f"Quantidade de pedidos aguardando: {len(self.itens)}")
        return len(self.itens)

    def esta_vazia(self):
        return len(self.itens) == 0
