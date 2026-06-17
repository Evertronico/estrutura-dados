from estruturas.fila import Fila
from estruturas.lista_encadeada import ListaEncadeada
from modelos.entidades import Compromisso, Contato

class ModuloAgenda:
    def __init__(self):
        self.fila_compromissos = Fila()
        self.lista_contatos = ListaEncadeada()

    def menu_agenda(self):
        while True:
            print('=' * 50)
            print('||    <<<<<<<<<<<MENU AGENDA PESSOAL>>>>>>>>>    ||')
            print('||    1) - ADICIONAR COMPROMISSO (FILA).....:    ||')
            print('||    2) - REALIZAR PRÓXIMO COMPROMISSO.....:    ||')
            print('||    3) - VER PRÓXIMO COMPROMISSO..........:    ||')
            print('||    4) - ADICIONAR CONTATO (L. ENCADEADA).:    ||')
            print('||    5) - BUSCAR CONTATO...................:    ||')
            print('||    6) - REMOVER CONTATO..................:    ||')
            print('||    7) - EXIBIR TUDO......................:    ||')
            print('||    8) - VOLTAR...........................:    ||')
            print('=' * 50)
            
            op = input("- ")
            if op == '1':
                t = input("Título: ")
                h = input("Hora: ")
                self.fila_compromissos.enfileirar(Compromisso(t, h))
            elif op == '2':
                item = self.fila_compromissos.desenfileirar()
                print(f"Realizado: {item}" if item else "Fila vazia")
            elif op == '3':
                item = self.fila_compromissos.consulta_primeiro()
                print(f"Próximo: {item}" if item else "Fila vazia")
            elif op == '4':
                n = input("Nome: ")
                t = input("Telefone: ")
                self.lista_contatos.inserir(Contato(n, t))
            elif op == '5':
                n = input("Nome para buscar: ")
                item = self.lista_contatos.buscar(lambda c: c.nome == n)
                print(item if item else "Não encontrado")
            elif op == '6':
                n = input("Nome para remover: ")
                item = self.lista_contatos.remover(lambda c: c.nome == n)
                print(f"Removido: {item}" if item else "Não encontrado")
            elif op == '7':
                print("\n--- Compromissos ---")
                for c in self.fila_compromissos.exibir(): print(c)
                print("\n--- Contatos ---")
                for c in self.lista_contatos.exibir(): print(c)
            elif op == '8':
                break
