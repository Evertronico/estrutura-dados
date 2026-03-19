# Função que cria o TDA Estoque
def criar_estoque():
    # Estrutura interna que armazena produtos e quantidades
    estoque = {}

    # Operação de entrada de produtos no estoque
    def entrada(produto, quantidade):
        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade

    # Operação de saída de produtos do estoque
    def saida(produto, quantidade):
        if produto in estoque and estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
        else:
            print("Estoque insuficiente ou produto inexistente.")

    # Operação de consulta do estoque de um produto
    def consultar(produto):
        return estoque.get(produto, 0)

    # Operação de listagem do estoque completo
    def listar():
        return estoque.copy()

    # Retorno das operações que definem o TDA
    return entrada, saida, consultar, listar

# Criação do TDA Estoque
entrada, saida, consultar, listar = criar_estoque()

# Uso das operações do TDA para manipular o estoque
entrada("Teclado", 10)
entrada("Mouse", 20)
entrada("Monitor", 5)

# Realização de saídas de produtos
saida("Mouse", 3)
saida("Teclado", 2)

# Consulta de informações específicas
print("Estoque do Mouse:", consultar("Mouse"))
print("Estoque do Teclado:", consultar("Teclado"))

# Listagem do estado geral do estoque
print("Estoque geral:", listar())
