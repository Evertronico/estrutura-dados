from Container import Container

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, container):
        self.itens.append(container)
        print(f"Container {container.id_container} empilhado.")

    def desempilhar(self):
        if not self.esta_vazia():
            container = self.itens.pop()
            print(f"Container {container.id_container} desempilhado.")
            return container
        print("Pilha vazia. Nenhum container para desempilhar.")
        return None

    def exibir_topo(self):
        if not self.esta_vazia():
            print(f"Container no topo: {self.itens[-1].id_container}")
            return self.itens[-1]
        print("Pilha vazia. Nenhum container no topo.")
        return None

    def exibir_todos(self):
        if self.esta_vazia():
            print("Pilha de containers vazia.")
            return
        print("Containers na pilha (do topo para a base):")
        for i in range(len(self.itens) - 1, -1, -1):
            print(f"  {self.itens[i].id_container}")

    def quantidade_armazenada(self):
        print(f"Quantidade de containers armazenados: {len(self.itens)}")
        return len(self.itens)

    def esta_vazia(self):
        return len(self.itens) == 0
