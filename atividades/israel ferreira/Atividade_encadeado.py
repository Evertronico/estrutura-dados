class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:

    def __init__(self):
        # referência para o primeiro nó
        self.head = None

    def inserir_inicio(self, valor):
        novo = No(valor)

        # o novo nó aponta para o antigo primeiro nó
        novo.proximo = self.head

        # atualiza a cabeça da lista
        self.head = novo

    def exibir(self):

        atual = self.head

        while atual:
            print(atual.dado)
            atual = atual.proximo

    def inserir_final(self, valor):

        novo = No(valor)

        if self.head is None:
            self.head = novo
            return

        atual = self.head

        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo
    
    def remover(self, valor):

        atual = self.head
        anterior = None

        while atual:

            if atual.dado == valor:

                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                return

            anterior = atual
            atual = atual.proximo

lista =  ListaEncadeada()

while True:
    print('=' * 50)
    print('||    <<<<<<<<<<<<MENU DE OPÇÕES>>:>>>>>>>>>    ||')
    print('||    1) -INSERIR INICIO...................:    ||')
    print('||    2) -INSERIR FIM......................:    ||')
    print('||    3) -REMOVER .........................:    ||')
    print('||    4) -EXIBIR...........................:    ||')
    print('||    5) -SAIR.............................:    ||')
    print('=' * 50)

    opcaoP = input("- ")
    print("-"*50)
    if opcaoP == "1":
        valor = int(input("INSERIR INICIO: "))
        lista.inserir_inicio(valor)
    elif opcaoP == "2":
        valor = int(input("INSERIR FINAL: "))
        lista.inserir_final(valor)
    elif opcaoP == "3":
        valor = int(input("REMOVER VALOR: "))
        lista.remover(valor)
    elif opcaoP == "4":
        print ("Valores na Lista:\n")
        lista.exibir()
        
    elif opcaoP == "5":
            print('Saindo...')
            break
    else:
            print('Opção inválida. Tente novamente')

