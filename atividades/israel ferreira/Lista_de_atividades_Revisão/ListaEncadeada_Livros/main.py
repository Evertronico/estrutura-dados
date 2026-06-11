from ListaLivros import ListaLivros
from Livro import Livro

def menu():
    print('=' * 50)
    print('||    <<<<<<<<<<<<MENU DE CONTROLE DE LIVROS>>>>>>>>>>    ||')
    print('||    1) - INSERIR LIVRO...................:    ||')
    print('||    2) - BUSCAR LIVRO....................:    ||')
    print('||    3) - REMOVER LIVRO...................:    ||')
    print('||    4) - EXIBIR TODOS OS LIVROS..........:    ||')
    print('||    5) - QUANTIDADE DE LIVROS............:    ||')
    print('||    6) - SAIR............................:    ||')
    print('=' * 50)

def main():
    lista_livros = ListaLivros()

    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            isbn = input("ISBN do Livro: ")
            novo_livro = Livro(titulo, autor, isbn)
            lista_livros.inserir_final(novo_livro)
            print(f"Livro '{titulo}' inserido com sucesso!")
        elif opcao == "2":
            titulo = input("Título do Livro para buscar: ")
            livro_encontrado = lista_livros.buscar_livro(titulo)
            if livro_encontrado:
                print("Livro encontrado:")
                print(livro_encontrado)
            else:
                print(f"Livro com título '{titulo}' não encontrado.")
        elif opcao == "3":
            titulo = input("Título do Livro para remover: ")
            if lista_livros.remover_livro(titulo):
                print(f"Livro '{titulo}' removido com sucesso!")
            else:
                print(f"Livro com título '{titulo}' não encontrado.")
        elif opcao == "4":
            print("Livros Emprestados:\n")
            lista_livros.exibir_livros()
        elif opcao == "5":
            print(f"Quantidade total de livros cadastrados: {lista_livros.quantidade_livros()}")
        elif opcao == "6":
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')
        print("\n")

if __name__ == "__main__":
    main()
