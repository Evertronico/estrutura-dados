class Cliente:
    def __init__(self, nome, id_cliente):
        self.nome = nome
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Cliente: {self.nome} (ID: {self.id_cliente})"
