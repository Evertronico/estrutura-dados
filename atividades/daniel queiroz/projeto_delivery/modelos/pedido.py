
# pedido feito por um cliente.
#
# O histórico de status do pedido é controlado por uma PILHA, pois a
# regra de "desfazer o último status" segue a lógica LIFO
# =====================================================================

from estruturas.pilha import Pilha


class Pedido:
    def __init__(self, numero, cliente, itens):
        self.numero = numero          # número sequencial do pedido
        self.cliente = cliente        # objeto Cliente que fez o pedido
        self.itens = itens            # lista de objetos Produto

        # Pilha que guarda o histórico de status do pedido.
        # O topo da pilha é sempre o status ATUAL.
        self.status = Pilha()
        self.status.empilhar("Recebido")

    # Soma o preço de todos os itens do pedido
    def valor_total(self):
        total = 0.0
        for item in self.itens:
            total += item.preco
        return total

    # Retorna o status atual (topo da pilha)
    def status_atual(self):
        return self.status.topo()

    # Avança o pedido para um novo status (empilha)
    def avancar_status(self, novo_status):
        self.status.empilhar(novo_status)

    # Desfaz o último status aplicado (desempilha), mantendo ao menos um
    def desfazer_status(self):
        # Não permite remover o status inicial "Recebido"
        if self.status.tamanho() <= 1:
            return None
        return self.status.desempilhar()

    def __str__(self):
        nomes_itens = ", ".join(item.nome for item in self.itens)
        return (f"Pedido #{self.numero} | Cliente: {self.cliente.nome} | "
                f"Itens: {nomes_itens} | Total: R$ {self.valor_total():.2f} | "
                f"Status: {self.status_atual()}")
