# classe para verificação de expressão matemática
class verificadorExpressao:
    
    def __init__(self):
        # pilha utilizada na verificação
        self.pilha = []
    
    # verifica se expreção e valida 
    def verificar(self, expressao):
        
        # percorre cada caractere da expressão
        for caractere in expressao:
            
            # empilha quando encontrar um parêntese de abertura
            if caractere in "(":
                self.pilha.append(caractere)
                
            #desenpilha quando encontrar um parêntese de fechamento 
            elif caractere in ")":
                
                # erro caso tenha um fechamento de parenteses sem abertura
                if len(self.pilha) == 0:
                    return False
                
                self.pilha.pop()
                
        # se a pilha estiver vazia a expressão e válida
        return len(self.pilha) == 0