class ListaNums:
    def __init__(self):
        self.lista = []

    def inserir(self, num):
        self.lista.append(num)

    def excluir(self, num):
        if num in self.lista:
            self.lista.remove(num)
        else:
            print("Esse número não foi encontrado")

    def pesquisar(self, num):
        if num in self.lista:
            return True
        else:
            return False
        
    def mostrar(self):
        print("Números da lista: ", self.lista)


    
def menu():
    lista = ListaNums()

    while True:
        print("Menu:")
        print("1 - Inserir número")
        print("2 - Remover número")
        print("3 - Pesquisar número")
        print("4 - Exibir todos")
        print("5 - Sair")
        opcao = int(input("Escolha uma das opções acima: "))

        if opcao == 1:
            num = int(input("Digite um número para adicionar: "))

            lista.inserir(num)
        elif opcao == 2:
            num = int(input("Digite o número a ser removido: "))
            lista.excluir(num)
        elif opcao == 3:
            num = int(input("Pesquise um número na lista: "))

            if lista.pesquisar(num):
                print(f"O número {num} faz parte da lista")
            else:
                print("Este número não faz parte da lista")

        elif opcao == 4:
            lista.mostrar()

        elif opcao == 5:
            break
        else:
            print("Opção inválida, digite um dos números das opções")
        

menu()