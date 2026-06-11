from NoDuplo import NoDuplo

class GaleriaFotos:
    def __init__(self):
        self.head = None
        self.tail = None
        self.atual = None  # Ponteiro para a foto atual
        self.tamanho = 0

    def adicionar_foto(self, nome_foto):
        novo_no = NoDuplo(nome_foto)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
            self.atual = novo_no  # Define a primeira foto como a atual
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
            self.tail = novo_no
        self.tamanho += 1

    def avancar_foto(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            return True
        return False

    def voltar_foto(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            return True
        return False

    def exibir_foto_atual(self):
        if self.atual:
            return f"Foto Atual: {self.atual.dado}"
        return "Nenhuma foto na galeria."

    def exibir_galeria(self):
        if self.head is None:
            print("Galeria vazia.")
            return
        temp = self.head
        fotos = []
        while temp:
            fotos.append(temp.dado)
            temp = temp.proximo
        print("Galeria Completa:", " <-> ".join(fotos))

    def informar_posicao_atual(self):
        if self.atual is None:
            return "Nenhuma foto selecionada."
        
        posicao = 0
        temp = self.head
        while temp:
            if temp == self.atual:
                return f"Posição Atual: {posicao + 1} de {self.tamanho}"
            posicao += 1
            temp = temp.proximo
        return "Posição não encontrada (erro interno)."

    def esta_vazia(self):
        return self.head is None
