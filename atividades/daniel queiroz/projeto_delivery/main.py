# =====================================================================
# SISTEMA DE DELIVERY - Projeto de Estrutura de Dados
# Aluno: Daniel Queiroz
#
# Arquivo principal: exibe o menu e conecta o usuário ao SistemaDelivery.
# Para executar, dentro da pasta "projeto_delivery", rode:
#       python main.py
# =====================================================================

from sistema.delivery import SistemaDelivery


# Carrega alguns dados de exemplo para o sistema já iniciar populado
def carregar_dados_exemplo(sistema):
    # Clientes (lista sequencial)
    sistema.cadastrar_cliente(1, "Ana Souza", "9999-0001", "Rua das Flores, 100")
    sistema.cadastrar_cliente(2, "Carlos Lima", "9999-0002", "Av. Brasil, 250")
    sistema.cadastrar_cliente(3, "Marina Dias", "9999-0003", "Rua Verde, 30")

    # Produtos (lista encadeada)
    sistema.adicionar_produto(101, "Pizza Calabresa", 45.00, "Lanche")
    sistema.adicionar_produto(102, "Hambúrguer Duplo", 28.50, "Lanche")
    sistema.adicionar_produto(103, "Refrigerante Lata", 6.00, "Bebida")
    sistema.adicionar_produto(104, "Pudim", 12.00, "Sobremesa")


def ler_int(mensagem):
    # Lê um número inteiro do usuário, tratando entradas inválidas
    try:
        return int(input(mensagem))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        return None


def menu_clientes(sistema):
    print("\n--- CLIENTES (Lista Sequencial) ---")
    print("1 - Cadastrar cliente")
    print("2 - Buscar cliente")
    print("3 - Remover cliente")
    print("4 - Listar clientes")
    opcao = input("Opção: ")

    if opcao == "1":
        id_cliente = ler_int("ID: ")
        if id_cliente is None:
            return
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        sistema.cadastrar_cliente(id_cliente, nome, telefone, endereco)
    elif opcao == "2":
        id_cliente = ler_int("ID do cliente: ")
        cliente = sistema.buscar_cliente(id_cliente)
        print(cliente if cliente else "Cliente não encontrado.")
    elif opcao == "3":
        id_cliente = ler_int("ID do cliente: ")
        sistema.remover_cliente(id_cliente)
    elif opcao == "4":
        sistema.clientes.exibir()
    else:
        print("Opção inválida.")


def menu_cardapio(sistema):
    print("\n--- CARDÁPIO (Lista Encadeada) ---")
    print("1 - Adicionar produto")
    print("2 - Buscar produto")
    print("3 - Remover produto")
    print("4 - Exibir cardápio")
    opcao = input("Opção: ")

    if opcao == "1":
        codigo = ler_int("Código: ")
        if codigo is None:
            return
        nome = input("Nome: ")
        try:
            preco = float(input("Preço: "))
        except ValueError:
            print("Preço inválido.")
            return
        categoria = input("Categoria: ")
        sistema.adicionar_produto(codigo, nome, preco, categoria)
    elif opcao == "2":
        codigo = ler_int("Código do produto: ")
        produto = sistema.buscar_produto(codigo)
        print(produto if produto else "Produto não encontrado.")
    elif opcao == "3":
        codigo = ler_int("Código do produto: ")
        sistema.remover_produto(codigo)
    elif opcao == "4":
        sistema.cardapio.exibir()
    else:
        print("Opção inválida.")


def menu_pedidos(sistema):
    print("\n--- PEDIDOS (Fila de preparo) ---")
    print("1 - Criar pedido")
    print("2 - Ver próximo da fila")
    print("3 - Exibir fila de preparo")
    print("4 - Finalizar próximo pedido (vai para o histórico)")
    opcao = input("Opção: ")

    if opcao == "1":
        id_cliente = ler_int("ID do cliente: ")
        if id_cliente is None:
            return
        entrada = input("Códigos dos produtos (separados por vírgula): ")
        codigos = []
        for parte in entrada.split(","):
            parte = parte.strip()
            if parte.isdigit():
                codigos.append(int(parte))
        sistema.criar_pedido(id_cliente, codigos)
    elif opcao == "2":
        pedido = sistema.proximo_da_fila()
        print(pedido if pedido else "Fila vazia.")
    elif opcao == "3":
        sistema.fila_preparo.exibir()
    elif opcao == "4":
        sistema.finalizar_proximo_pedido()
    else:
        print("Opção inválida.")


def menu_status(sistema):
    print("\n--- STATUS DO PEDIDO (Pilha) ---")
    print("Escolha um pedido da fila de preparo para alterar o status.")
    if sistema.fila_preparo.esta_vazia():
        print("Não há pedidos na fila.")
        return

    sistema.fila_preparo.exibir()
    numero = ler_int("Número do pedido: ")

    # Procura o pedido na fila pelo número
    pedido = None
    for p in sistema.fila_preparo.itens:
        if p.numero == numero:
            pedido = p
            break

    if pedido is None:
        print("Pedido não encontrado na fila.")
        return

    print(f"Status atual (topo da pilha): {pedido.status_atual()}")
    print("1 - Avançar status")
    print("2 - Desfazer último status")
    opcao = input("Opção: ")

    if opcao == "1":
        novo = input("Novo status: ")
        pedido.avancar_status(novo)
        print(f"Status atual: {pedido.status_atual()}")
    elif opcao == "2":
        desfeito = pedido.desfazer_status()
        if desfeito is None:
            print("Não é possível desfazer o status inicial.")
        else:
            print(f"Status '{desfeito}' desfeito. Status atual: {pedido.status_atual()}")
    else:
        print("Opção inválida.")


def menu_historico(sistema):
    print("\n--- HISTÓRICO (Lista Duplamente Encadeada) ---")
    print("1 - Exibir do mais antigo ao mais recente")
    print("2 - Exibir do mais recente ao mais antigo")
    print("3 - Navegar para frente (próximo)")
    print("4 - Navegar para trás (anterior)")
    print("5 - Ver pedido atual do cursor")
    opcao = input("Opção: ")

    if opcao == "1":
        sistema.historico.exibir_frente()
    elif opcao == "2":
        sistema.historico.exibir_tras()
    elif opcao == "3":
        pedido = sistema.historico.avancar()
        if pedido:
            print(f">> {pedido}")
    elif opcao == "4":
        pedido = sistema.historico.voltar()
        if pedido:
            print(f"<< {pedido}")
    elif opcao == "5":
        pedido = sistema.historico.atual_pedido()
        print(pedido if pedido else "Histórico vazio.")
    else:
        print("Opção inválida.")


def main():
    sistema = SistemaDelivery()
    print("Carregando dados de exemplo...\n")
    carregar_dados_exemplo(sistema)

    while True:
        print("\n========= SISTEMA DE DELIVERY =========")
        print("1 - Clientes        (Lista Sequencial)")
        print("2 - Cardápio        (Lista Encadeada)")
        print("3 - Pedidos         (Fila)")
        print("4 - Status do pedido(Pilha)")
        print("5 - Histórico       (Lista Duplamente Encadeada)")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes(sistema)
        elif opcao == "2":
            menu_cardapio(sistema)
        elif opcao == "3":
            menu_pedidos(sistema)
        elif opcao == "4":
            menu_status(sistema)
        elif opcao == "5":
            menu_historico(sistema)
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
