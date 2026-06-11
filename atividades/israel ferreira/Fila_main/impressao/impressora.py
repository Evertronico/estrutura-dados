class Impressora:
    
    def __init__(self):
        # fila de impressao
        self.documento = []
        
    def adicionar_documento(self, documento):
        self.documento.append(documento)
        print (f"Documento {documento} adicionado a fila")
        
    def imprimir(self):
        if len(self.documento) == 0:
            print("nenhum documento para imprimir")
            return
        documento = self.documentos.pop(0)
        print(f'imprimindo: {documento}')
   
    def exibir_fila(self):
        if len(self.documentos) == 0:
            print("nenhum documento para imprimir")
        else:
            print("Documentos na fila:")
            for doc in self.documentos:
                print(f" - {doc}")
                