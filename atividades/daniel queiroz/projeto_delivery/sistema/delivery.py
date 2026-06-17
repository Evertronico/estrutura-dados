
# Classe central: SistemaDelivery


from estruturas.lista_sequencial import ListaSequencialClientes
from estruturas.lista_encadeada import Cardapio
from estruturas.lista_duplamente_encadeada import HistoricoPedidos
from estruturas.fila import Fila

from modelos.cliente import Cliente
from modelos.produto import Produto
from modelos.pedido import Pedido


class SistemaDelivery:
    def __init__(self):
        # LISTA SEQUENCIAL -> cadastro de clientes
        self.clientes = ListaSequencialClientes()

        # LISTA ENCADEADA -> cardápio de produtos
        self.cardapio = Cardapio()

        # FILA -> pedidos aguardando preparo (ordem de chegada)
        self.fila_preparo = Fila()

        # LISTA DUPLAMENTE ENCADEADA -> histórico de pedidos entregues
        self.historico = HistoricoPedidos()

        # Contador para gerar números de pedido automaticamente
        self.proximo_numero_pedido = 1

    def cadastrar_cliente(self, id_cliente, nome, telefone, endereco):
        cliente = Cliente(id_cliente, nome, telefone, endereco)
        self.clientes.inserir(cliente)

    def buscar_cliente(self, id_cliente):
        return self.clientes.buscar(id_cliente)

    def remover_cliente(self, id_cliente):
        return self.clientes.remover(id_cliente)

    # CARDÁPIO (lista encadeada) 
    def adicionar_produto(self, codigo, nome, preco, categoria):
        produto = Produto(codigo, nome, preco, categoria)
        self.cardapio.inserir(produto)
        print(f"Produto adicionado ao cardápio: {produto.nome}")

    def buscar_produto(self, codigo):
        return self.cardapio.buscar(codigo)

    def remover_produto(self, codigo):
        return self.cardapio.remover(codigo)

    # PEDIDOS (fila)
    # Cria um pedido para um cliente a partir de uma lista de códigos de produtos e o coloca na fila de preparo.
    def criar_pedido(self, id_cliente, codigos_produtos):
        cliente = self.buscar_cliente(id_cliente)
        if cliente is None:
            print("Não foi possível criar o pedido: cliente não encontrado.")
            return None

        # Monta a lista de produtos do pedido
        itens = []
        for codigo in codigos_produtos:
            produto = self.buscar_produto(codigo)
            if produto is None:
                print(f"Aviso: produto de código {codigo} não existe e foi ignorado.")
            else:
                itens.append(produto)

        if len(itens) == 0:
            print("Não foi possível criar o pedido: nenhum produto válido.")
            return None

        pedido = Pedido(self.proximo_numero_pedido, cliente, itens)
        self.proximo_numero_pedido += 1

        # Entra na fila de preparo (FIFO)
        self.fila_preparo.enfileirar(pedido)
        print(f"Pedido #{pedido.numero} criado e colocado na fila de preparo.")
        return pedido

    # Mostra qual é o próximo pedido a ser preparado
    def proximo_da_fila(self):
        return self.fila_preparo.primeiro()

    # Conclui o preparo do primeiro pedido da fila: ele avança de status, é marcado como entregue e vai para o histórico (lista dupla).
    def finalizar_proximo_pedido(self):
        pedido = self.fila_preparo.desenfileirar()
        if pedido is None:
            print("Não há pedidos na fila para finalizar.")
            return None

        # Avança os status usando a PILHA dentro do pedido
        pedido.avancar_status("Em preparo")
        pedido.avancar_status("Saiu para entrega")
        pedido.avancar_status("Entregue")

        # Registra no histórico de entregas (lista duplamente encadeada)
        self.historico.adicionar(pedido)
        print(f"Pedido #{pedido.numero} finalizado e enviado ao histórico.")
        return pedido
