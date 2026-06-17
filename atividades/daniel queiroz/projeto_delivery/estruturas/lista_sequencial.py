
# Estrutura: LISTA SEQUENCIAL
# Usada para o CADASTRO DE CLIENTES.

class ListaSequencialClientes:
    def __init__(self):
        self.itens = []

    # Insere um cliente no final da lista Complexidade O(1).
    def inserir(self, cliente):
        self.itens.append(cliente)
        print(f"Cliente cadastrado: {cliente.nome}")
    # Busca sequencial: percorre posição por posição até achar o id Complexidade O(n).
    def buscar(self, id_cliente):
        for i in range(len(self.itens)):
            if self.itens[i].id == id_cliente:
                return self.itens[i]   # encontrou: retorna o cliente
        return None                    # não encontrou

    # Remove o cliente pelo id. Para mostrar o funcionamento da lista sequencial, deslocamos manualmente os elementos seguintes uma Complexidade O(n). 
    def remover(self, id_cliente):
        indice = -1

        # localiza o índice do cliente
        for i in range(len(self.itens)):
            if self.itens[i].id == id_cliente:
                indice = i
                break

        if indice == -1:
            print("Cliente não encontrado para remoção.")
            return False

        removido = self.itens[indice]

        # desloca os elementos seguintes uma posição para trás
        for i in range(indice, len(self.itens) - 1):
            self.itens[i] = self.itens[i + 1]

        # remove a última posição que duplicou
        self.itens.pop()

        print(f"Cliente removido: {removido.nome}")
        return True

    # Exibe todos os clientes cadastrados
    def exibir(self):
        if len(self.itens) == 0:
            print("Nenhum cliente cadastrado.")
            return
        print("Clientes cadastrados")
        for cliente in self.itens:
            print(cliente)
