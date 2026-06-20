# Estrutura: FILA DE PRIORIDADE
# Os pacientes ficam ordenados pelo score (maior primeiro).


class FilaSaude:
    def __init__(self):
        self.itens = []

    # Insere o paciente já na posição certa, mantendo a ordem por score. O(n).
    def enfileirar(self, paciente):
        i = 0
        while i < len(self.itens) and self.itens[i].score() >= paciente.score():
            i += 1
        self.itens.insert(i, paciente)

    # Remove e retorna o paciente de maior prioridade (início da fila). O(n).
    def atender_proximo(self):
        if self.esta_vazia():
            return None
        return self.itens.pop(0)

    # Mostra o próximo sem remover
    def primeiro(self):
        if self.esta_vazia():
            return None
        return self.itens[0]

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

    # Exibe a fila com a posição de cada paciente
    def exibir(self):
        if self.esta_vazia():
            print("\nFila vazia.")
            return
        print("\n===== FILA ATUAL =====\n")
        for posicao, paciente in enumerate(self.itens, start=1):
            print(f"{posicao}º -> {paciente}")
