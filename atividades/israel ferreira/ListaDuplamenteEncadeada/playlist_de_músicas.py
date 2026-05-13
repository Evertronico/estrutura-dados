'''
    Implemente um sistema de playlist de músicas onde o usuário pode navegar para frente e para trás entre as músicas.
    Requisitos: 
        Inserir música no final
        Avançar música
        Voltar música
        Exibir playlist completa
'''
from No import No

class ListaDupla:
    def __init__(self):
        self.head = None
        self.tail = None
        self.atual = None  # música atual

    def inserir_inicio(self, _):  # usado no menu como "Avançar música"
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            print(f"Avançou -> Tocando agora: {self.atual.dado}")
        else:
            print("Não há próxima música.")

    def inserir_final(self, dado):  # usado no menu como "Inserir música no final"
        novo = No(dado)
        if self.head is None:
            self.head = self.tail = novo
            self.atual = novo
        else:
            self.tail.proximo = novo
            novo.anterior = self.tail
            self.tail = novo

    def buscar(self, _):  # usado no menu como "Voltar música"
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            print(f"Voltou -> Tocando agora: {self.atual.dado}")
        else:
            print("Não há música anterior.")

    def exibir(self):  # usado no menu como "Exibir playlist"
        atual = self.head
        print("Playlist completa:")
        while atual:
            marcador = " <= Tocando" if atual == self.atual else ""
            print(f"- {atual.dado}{marcador}")
            atual = atual.proximo


# Função de menu
def menu():
    print('=' * 50)
    print('||    <<<<<<<<<<<<MENU DE OPÇÕES>>:>>>>>>>>>    ||')
    print('||    1) -INSERIR MÚSICA FINAL.............:    ||')
    print('||    2) -AVANÇAR MÚSICA...................:    ||')
    print('||    3) -VOLTAR MÚSICA....................:    ||')
    print('||    4) -EXIBIR PLAYLIST..................:    ||')
    print('||    5) -SAIR.............................:    ||')
    print('=' * 50)

def main():
    lista_dados = ListaDupla()
    
    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)
        
        if opcao == "1":
            valor = input("Nome da música: ")
            ListaDupla.inserir_final(lista_dados, valor)
            
        elif opcao == "2":
            ListaDupla.inserir_inicio(lista_dados, None)
            
        elif opcao == "3":
            ListaDupla.buscar(lista_dados, None)
                
        elif opcao == "4":
            ListaDupla.exibir(lista_dados)
            
        elif opcao == "5":
            print("Saindo...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")


# Inicialização
if __name__ == "__main__":
    main()
