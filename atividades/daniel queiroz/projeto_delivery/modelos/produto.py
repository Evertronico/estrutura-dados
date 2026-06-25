# Modelo do Produto
# Representa um item do cardápio do delivery

class Produto:
    def __init__(self, codigo, nome, preco, categoria):
        self.codigo = codigo          # código único do produto
        self.nome = nome              # nome do produto
        self.preco = preco            # preço unitário (float)
        self.categoria = categoria    # categoria (Lanche, Bebida, Sobremesa...)

    def __str__(self):
        return f"#{self.codigo} - {self.nome} ({self.categoria}) - R$ {self.preco:.2f}"
