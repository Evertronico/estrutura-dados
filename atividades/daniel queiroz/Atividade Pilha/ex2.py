class Investigacao:
    def __init__(self):
        self.pilha_evidencias = []

    def registrar_evidencia(self, evidencia):
        self.pilha_evidencias.append(evidencia)
        print(f"Evidência coletada: {evidencia}")

    def pilha_vazia(self):
        return len(self.pilha_evidencias) == 0

    def exibir_historico(self):
        if self.pilha_vazia():
            print("Status: Nenhuma evidência coletada na cena do crime.")
        else:
            print("Status: Histórico de Evidências (Análise Reversa):")
            for evidencia in reversed(self.pilha_evidencias):
                print(f"  -> {evidencia}")

    def analisar_evidencia(self):
        if self.pilha_vazia():
            print("Aviso: Todas as evidências já foram analisadas ou a cena está limpa.")
            return None
        
        evidencia_em_analise = self.pilha_evidencias.pop()
        print(f"Enviando para o laboratório: '{evidencia_em_analise}'")
        return evidencia_em_analise

if __name__ == "__main__":
    print("INICIANDO INVESTIGAÇÃO NA CENA DO CRIME\n")
    pericia = Investigacao()

    print("--- Fase de Coleta ---")
    pericia.registrar_evidencia("1. Pegadas com barro na porta da frente")
    pericia.registrar_evidencia("2. Vidro quebrado próximo à janela da sala")
    pericia.registrar_evidencia("3. Fio de cabelo encontrado no tapete")
    pericia.registrar_evidencia("4. Ferramenta pé-de-cabra caída no corredor")
    pericia.registrar_evidencia("5. Impressão digital fresca no cofre aberto")

    print("\n--- Fechamento da Cena do Crime ---")
    pericia.exibir_historico()

    print("\n--- Fase de Análise Laboratorial ---")
    print("O investigador começa a analisar da evidência mais recente (cofre) tentando traçar os passos de volta até a entrada.\n")

    while not pericia.pilha_vazia():
        pericia.analisar_evidencia()

    print("\n--- Status Final ---")
    pericia.exibir_historico()
    print("\nTodas as evidências foram processadas. O relatório final está pronto para o detetive.")