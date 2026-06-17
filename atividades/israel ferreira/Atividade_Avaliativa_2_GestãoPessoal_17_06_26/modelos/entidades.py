class Compromisso:
    def __init__(self, titulo, hora):
        self.titulo = titulo
        self.hora = hora
    def __str__(self):
        return f"[{self.hora}] {self.titulo}"

class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
    def __str__(self):
        return f"Projeto: {self.nome} - {self.descricao}"

class Transacao:
    def __init__(self, descricao, valor, tipo):
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
    def __str__(self):
        simbolo = "+" if self.tipo == 'Entrada' else "-"
        return f"{self.tipo}: {self.descricao} | {simbolo}R${self.valor:.2f}"

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    def __str__(self):
        return f"{self.nome}: {self.telefone}"
