class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    
    
    def inserir_final(self, valor):
        valor = float(valor)
        novo_no = No(valor)
        
        if self.inicio is None:
            self.inicio = novo_no
            print(f"Elemento {valor} inserido no início da lista")
        else:
            atual = self.inicio
            
            while atual.proximo is not None:
                atual = atual.proximo
            
            atual.proximo = novo_no
            print(f"Elemento {valor} inserido no final da lista")
    
    
    def buscar(self, valor):
        valor = float(valor)
        atual = self.inicio
        posicao = 0
        encontrado = False
        
        while atual is not None:
            if atual.valor == valor:
                encontrado = True
                print(f"Elemento {valor} encontrado na posição {posicao}")
                return True
            atual = atual.proximo
            posicao += 1
        
        if not encontrado:
            print(f"Elemento {valor} não encontrado")
            return False
    
    
    def exibir(self):
        if self.inicio is None:
            print("Lista vazia!")
        else:
            atual = self.inicio
            saida = ""
            posicao = 0
            
            while atual is not None:
                saida = saida + f"[{posicao}]={atual.valor} -> "
                atual = atual.proximo
                posicao += 1
            
            saida = saida + "None"
            print("Lista: " + saida)
            print(f"Total de elementos: {posicao}")
    
    
    def remover(self, valor):
        valor = float(valor)
        if self.inicio is None:
            print("Lista vazia!")
            return False
        
        if self.inicio.valor == valor:
            self.inicio = self.inicio.proximo
            print(f"Elemento {valor} removido do início")
            return True
        
        atual = self.inicio
        anterior = None
        
        while atual is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                print(f"Elemento {valor} removido")
                return True
            anterior = atual
            atual = atual.proximo
        
        print(f"Elemento {valor} não encontrado")
        return False
    
    
    def limpar(self):
        self.inicio = None
        print("Lista limpa com sucesso!")


def menu(lista):
    ativo = True
    
    while ativo:
        print("\n" + "=" * 50)
        print("Lista Encadeada Simples")
        print("=" * 50)
        print("1. Inserir elemento no final")
        print("2. Buscar elemento")
        print("3. Remover elemento")
        print("4. Exibir lista")
        print("5. Limpar lista")
        print("0. Sair")
        print("=" * 50)
        
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                valor = input("Digite o valor a inserir: ")
                lista.inserir_final(valor)
            
            case "2":
                valor = input("Digite o valor a buscar: ")
                lista.buscar(valor)
            
            case "3":
                valor = input("Digite o valor a remover: ")
                lista.remover(valor)
            
            case "4":
                lista.exibir()
            
            case "5":
                confirmar = input("Tem certeza? (s/n): ")
                if confirmar.lower() == "s":
                    lista.limpar()
            
            case "0":
                print("Encerrando o programa...")
                ativo = False
            
            case _:
                print("Opção inválida! Tente novamente.")


lista = ListaEncadeada()
executando = True

while executando:
    menu(lista)
    executando = False
