from estruturas.lista_sequencial import ListaSequencial
from modelos.entidades import Transacao

class ModuloFinanceiro:
    def __init__(self):
        self.lista_transacoes = ListaSequencial()

    def menu_financeiro(self):
        while True:
            print('=' * 50)
            print('||    <<<<<<<<<<<GESTÃO FINANCEIRA>>>>>>>>>>     ||')
            print('||    1) - REGISTRAR ENTRADA................:    ||')
            print('||    2) - REGISTRAR SAÍDA..................:    ||')
            print('||    3) - BUSCAR TRANSAÇÃO.................:    ||')
            print('||    4) - REMOVER TRANSAÇÃO................:    ||')
            print('||    5) - EXIBIR EXTRATO...................:    ||')
            print('||    6) - VOLTAR...........................:    ||')
            print('=' * 50)
            
            op = input("- ")
            if op == '1' or op == '2':
                d = input("Descrição: ")
                v = float(input("Valor: "))
                t = 'Entrada' if op == '1' else 'Saída'
                self.lista_transacoes.inserir(Transacao(d, v, t))
            elif op == '3':
                d = input("Descrição para buscar: ")
                item = self.lista_transacoes.buscar(lambda t: t.descricao == d)
                print(item if item else "Não encontrado")
            elif op == '4':
                d = input("Descrição para remover: ")
                item = self.lista_transacoes.remover(lambda t: t.descricao == d)
                print(f"Removido: {item}" if item else "Não encontrado")
            elif op == '5':
                saldo = 0
                print("\n--- Extrato Financeiro ---")
                for t in self.lista_transacoes.exibir():
                    print(t)
                    if t.tipo == 'Entrada': saldo += t.valor
                    else: saldo -= t.valor
                print(f"SALDO ATUAL: R${saldo:.2f}")
            elif op == '6':
                break
