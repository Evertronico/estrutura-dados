# importa a classe ListaEncadeada
from lista_encadeada import ListaEncadeada

# menu de opções da lista encadeada
def menu():
    print("\nMenu:")
    print("1. Inserir no início")
    print("2. Inserir no final")
    print("3. Remover elemento")
    print("4. Exibir lista")
    print("0. Sair")

def main():
    # cria um objeto da lista encadeada
    lista = ListaEncadeada()

    # loop infinito
    while True:
        # exibe o menu de opções
        menu()
        # solicita a opção do usuário
        opcao = input("Escolha uma opção: ")

        # verifica se a opção é inserir no início
        if opcao == "1":
            valor = int(input("Digite o valor:"))
            lista.inserir_inicio(valor)
            print("Valor inserido no início")
    
        # verifica se a opção é inserir no final
        elif opcao == "2":
            valor = int(input("Digite o valor:"))
            lista.inserir_final(valor)
            print("Valor inserido no final")

        # verifica se a opção é de remover
        elif opcao == "3":
            valor = int(input("Digite o valor a ser removido:"))
            lista.remover(valor)
            print("Valor removido (se existir)")

        # verifica se a opção é de exibir a lista
        elif opcao == "4":
            print("\nLista atual:")
            lista.exibir()

        # verifica se a opção é de sair
        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()