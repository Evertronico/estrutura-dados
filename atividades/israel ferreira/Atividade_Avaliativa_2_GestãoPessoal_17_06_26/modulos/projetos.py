from estruturas.lista_dupla import ListaDuplamenteEncadeada
from modelos.entidades import Projeto

class ModuloProjetos:
    def __init__(self):
        self.lista_projetos = ListaDuplamenteEncadeada()

    def menu_projetos(self):
        while True:
            atual = self.lista_projetos.obter_atual()
            print('=' * 50)
            print( '||    <<<<<<<<<<<<GESTÃO DE PROJETOS>>>>>>>>>>   ||')
            print(f'   ATUAL: {atual.nome if atual else "Nenhum":<33}  ')
            print( '||    1) - ADICIONAR PROJETO................:    ||')
            print( '||    2) - PRÓXIMO PROJETO..................:    ||')
            print( '||    3) - PROJETO ANTERIOR.................:    ||')
            print( '||    4) - VER DETALHES ATUAL...............:    ||')
            print( '||    5) - VOLTAR...........................:    ||')
            print('=' * 50)
            
            op = input("- ")
            if op == '1':
                n = input("Nome do Projeto: ")
                d = input("Descrição: ")
                self.lista_projetos.inserir(Projeto(n, d))
            elif op == '2':
                item = self.lista_projetos.navegar_proximo()
                if not item: print("Fim da lista")
            elif op == '3':
                item = self.lista_projetos.navegar_anterior()
                if not item: print("Início da lista")
            elif op == '4':
                print(atual if atual else "Nenhum projeto cadastrado")
            elif op == '5':
                break
