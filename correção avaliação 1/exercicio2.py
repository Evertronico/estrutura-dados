def inserir(lista, valor):
    lista.append(valor)

def remover(lista, valor):
    if valor in lista:
        lista.remove(valor)
        return True
    return False

def buscar(lista, valor):
    return valor in lista

def exibir(lista):
    print(f"Lista atual: {lista}")

def menu():
    dados = []
    while True:
        print("\n--- MENU TAD LISTA ---")
        print("1. Inserir")
        print("2. Remover")
        print("3. Buscar")
        print("4. Exibir")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            v = int(input("Valor para inserir: "))
            inserir(dados, v)
        elif opcao == '2':
            v = int(input("Valor para remover: "))
            if remover(dados, v): print("Removido com sucesso.")
            else: print("Valor não encontrado.")
        elif opcao == '3':
            v = int(input("Valor para buscar: "))
            if buscar(dados, v): print("O elemento existe na lista.")
            else: print("O elemento não existe.")
        elif opcao == '4':
            exibir(dados)
        elif opcao == '5':
            break

if __name__ == "__main__":
    menu()