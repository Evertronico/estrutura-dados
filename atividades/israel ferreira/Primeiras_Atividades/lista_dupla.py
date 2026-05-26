class No:
    def __init__(self, titulo):
        self.titulo = titulo
        self.anterior = None
        self.proximo = None

class Livro:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.atual = None

    def inserir_capitulo(self, titulo):
        novo_no = No(titulo)
        if not self.primeiro:
            self.primeiro = novo_no
            self.ultimo = novo_no
            self.atual = novo_no
        else:
            novo_no.anterior = self.ultimo
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no
        print(f"Capítulo '{titulo}' adicionado ao livro.")

    def proximo_capitulo(self):
        
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            
            self._mover_para_inicio(self.atual)
            self.exibir_capitulo_atual()
        else:
            print("Aviso: Você já está no último capítulo disponível.")

    def capitulo_anterior(self):
        
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            
            self._mover_para_inicio(self.atual)
            self.exibir_capitulo_atual()
        else:
            print("Aviso: Você já está no primeiro capítulo disponível.")

    def exibir_capitulo_atual(self):
     
        if self.atual:
            print(f"Capítulo atual: {self.atual.titulo}")
        else:
            print("Nenhum capítulo carregado.")

    def _mover_para_inicio(self, no):
      
        if no == self.primeiro:
            return

        if no.anterior:
            no.anterior.proximo = no.proximo
        if no.proximo:
            no.proximo.anterior = no.anterior
        else:
            self.ultimo = no.anterior

        no.proximo = self.primeiro
        no.anterior = None
        if self.primeiro:
            self.primeiro.anterior = no
        self.primeiro = no

    def exibir_ordem_leitura(self):
        temp = self.primeiro
        ordem = []
        while temp:
            ordem.append(temp.titulo)
            temp = temp.proximo
        print("\n[Histórico/Ordem Atual]: " + " -> ".join(ordem))

if __name__ == "__main__":
    meu_livro = Livro()

    print("--- 1. Inserindo 5 Capítulos ---")
    meu_livro.inserir_capitulo("Introdução")
    meu_livro.inserir_capitulo("Capítulo 1: Variáveis")
    meu_livro.inserir_capitulo("Capítulo 2: Condicionais")
    meu_livro.inserir_capitulo("Capítulo 3: Repetição")
    meu_livro.inserir_capitulo("Conclusão")

    meu_livro.exibir_ordem_leitura()
    meu_livro.exibir_capitulo_atual()

    print("\n--- 2. Navegando para Frente ---")
    meu_livro.proximo_capitulo() 
    meu_livro.proximo_capitulo() 
    
    print("\n--- 3. Navegando para Trás ---")
    meu_livro.capitulo_anterior()

    print("\n--- 4. Testando Extremos ---")
    meu_livro.proximo_capitulo()
    meu_livro.proximo_capitulo()
    meu_livro.proximo_capitulo()
    meu_livro.proximo_capitulo() 


    print("\n--- 5. Estado Final da Estrutura ---")
    meu_livro.exibir_ordem_leitura()
