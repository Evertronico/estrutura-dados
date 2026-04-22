'''
    Implemente uma Lista Encadeada Simples em Python utilizando classes.

    A estrutura deve conter:
    Classe Node
    Atributos:

        valor

        próximo (referência)

    Classe ListaEncadeada
    Métodos:

        Inserir no final

        Buscar elemento

        Exibir lista
        
    Requisitos:
    Utilizar corretamente o conceito de referência entre nós
    Não utilizar listas Python como estrutura interna
    Demonstrar funcionamento no programa principal

'''
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def inserir_final(inicio, valor):
    novo_no = Node(valor)
    if inicio == None:
        print("Inserido primeiro elemento.")
        return novo_no
    atual = inicio
    while atual.proximo: 
        atual = atual.proximo
    atual.proximo = novo_no
    print(f"Valor {valor} inserido no final.")
    return inicio

def buscar(inicio, valor):
    atual = inicio
    posicao = 0
    while atual:
        if atual.valor == valor:
            return posicao
        atual = atual.proximo
        posicao += 1
    return -1

def remover(inicio, valor):
    atual = inicio
    anterior = None
    while atual: 
        if atual.valor == valor:
            if anterior == None:
                inicio = atual.proximo
            else:
                anterior.proximo = atual.proximo
            print(f"Valor {valor} removido.")
            return inicio
        anterior = atual
        atual = atual.proximo
    print("Valor não encontrado.")
    return inicio

def exibir(inicio):
    if inicio == None:
        print("A lista está vazia.")
        return
    atual = inicio
    print("Lista Encadeada:")
    while atual:
        print(f"[{atual.valor}]", end=" -> ")
        atual = atual.proximo
    print("None")

def menu():
    print("=" * 50)
    print("||    <<<<<<<<<<<< MENU DE OPÇÕES >>>>>>>>>>>    ||")
    print("||    1) Inserir no final....................    ||")
    print("||    2) Buscar elemento.....................    ||")
    print("||    3) Remover elemento....................    ||")
    print("||    4) Exibir lista........................    ||")
    print("||    5) Sair................................    ||")
    print("=" * 50)

def main():
    inicio = None
    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            valor = int(input("Informe o valor para inserir: "))
            inicio = inserir_final(inicio, valor)

        elif opcao == "2":
            valor = int(input("Informe o valor para buscar: "))
            posi = buscar(inicio, valor)
            if posi != -1:
                print(f"Valor {valor} encontrado na posição {posi}.")
            else:
                print("Valor não encontrado.")

        elif opcao == "3":
            valor = int(input("Informe o valor para remover: "))
            inicio = remover(inicio, valor)

        elif opcao == "4":
            exibir(inicio)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
