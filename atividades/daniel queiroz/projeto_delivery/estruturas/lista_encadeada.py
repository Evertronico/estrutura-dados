# =====================================================================
# Estrutura: LISTA ENCADEADA (simples)
# Usada para o CARDÁPIO de produtos.


class No:
    def __init__(self, produto):
        self.produto = produto    
        self.proximo = None      


class Cardapio:
    def __init__(self):
        self.head = None          

    # Inserção no final. Complexidade o(n)
    def inserir(self, produto):
        novo = No(produto)

        # Caso a lista esteja vazia, o novo nó vira o primeiro
        if self.head is None:
            self.head = novo
            return

        # Caminha até o último nó e o conecta ao novo
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo

    # Busca Complexidade O(N)
    def buscar(self, codigo):
        atual = self.head
        while atual:
            if atual.produto.codigo == codigo:
                return atual.produto
            atual = atual.proximo
        return None

    # remover 
    def remover(self, codigo):
        atual = self.head
        anterior = None

        while atual:
            if atual.produto.codigo == codigo:
                # Se for o primeiro nó, o head passa a ser o próximo
                if anterior is None:
                    self.head = atual.proximo
                else:
                    # "pula" o nó atual
                    anterior.proximo = atual.proximo
                print(f"Produto removido do cardápio: {atual.produto.nome}")
                return True
            anterior = atual
            atual = atual.proximo

        print("Produto não encontrado no cardápio.")
        return False

    # Exibição 
    def exibir(self):
        if self.head is None:
            print("Cardápio vazio.")
            return
        print("Cardápio ")
        atual = self.head
        while atual:
            print(atual.produto)
            atual = atual.proximo
