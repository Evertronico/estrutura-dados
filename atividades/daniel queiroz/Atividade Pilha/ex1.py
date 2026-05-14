class ControleLancamento:
    def __init__(self):
        # A lista atuará como a nossa estrutura de Pilha
        self.pilha_etapas = []

    def registrar_etapa(self, etapa):
        self.pilha_etapas.append(etapa)
        print(f"Etapa registrada: {etapa}")

    def pilha_vazia(self):
        
        return len(self.pilha_etapas) == 0

    def exibir_etapas(self):
        if self.pilha_vazia():
            print("Status: Nenhuma etapa registrada. A pilha está vazia.")
        else:
            print("Status: Etapas atuais na pilha (do topo/mais recente para a base):")
            for etapa in reversed(self.pilha_etapas):
                print(f"  -> {etapa}")

    def abortar_lancamento(self):
        if self.pilha_vazia():
            print("Erro ao abortar: Não há etapas para desfazer.")
            return None
        
        etapa_desfeita = self.pilha_etapas.pop()
        print(f" Desfazendo: '{etapa_desfeita}'")
        return etapa_desfeita



if __name__ == "__main__":
    print("INICIANDO PROTOCOLO DE LANÇAMENTO...\n")
    controle = ControleLancamento()

    #Simulando
    controle.registrar_etapa("1. Verificação de sistemas elétricos e comunicação")
    controle.registrar_etapa("2. Abastecimento de combustível (Oxigênio Líquido / RP-1)")
    controle.registrar_etapa("3. Embarque da tripulação / Fechamento da escotilha")
    controle.registrar_etapa("4. Retirada da torre de serviço (braço de acesso)")
    controle.registrar_etapa("5. Inicialização da sequência de ignição (T-10 segundos)")

    print("\n--- Verificação de Status Pré-Lançamento ---")
    controle.exibir_etapas()

    # Simulando um problema 
    print("\n ALARME: Anomalia de pressão detectada no motor 2 aos T-3 segundos!")
    print("INICIANDO PROCEDIMENTO DE ABORTO (SCRAM)!\n")

    # Abortando o lançamento desfazendo as etapas 

    while not controle.pilha_vazia():
        controle.abortar_lancamento()

    print("\n--- Verificação de Status Pós-Aborto ---")
    controle.exibir_etapas()
    print("\nProcedimento de segurança concluído. Tripulação e veículo seguros.")