
from construcao_sanduiche import Sanduiche


pedido = Sanduiche()

pedido.adicionar("Pão")
pedido.adicionar("Alface")
pedido.adicionar("Tomate")
pedido.adicionar("Queijo")
pedido.adicionar("Presunto")
pedido.adicionar("Molho especial")

pedido.exibir()

pedido.remover()
pedido.exibir()

pedido.adicionar("Bacon crocante")
pedido.exibir()

pedido.remover()
pedido.remover()
pedido.exibir()

