class Acao:
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return f"Ação: {self.descricao}"
