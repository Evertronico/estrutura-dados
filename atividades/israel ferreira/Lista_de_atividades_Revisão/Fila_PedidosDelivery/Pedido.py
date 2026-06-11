class Pedido:
    def __init__(self, id_pedido, descricao):
        self.id_pedido = id_pedido
        self.descricao = descricao

    def __str__(self):
        return f"Pedido ID: {self.id_pedido}, Descrição: {self.descricao}"
