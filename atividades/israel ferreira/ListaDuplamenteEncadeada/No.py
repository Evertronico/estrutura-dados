# Representa um nó na lista duplamente encadeada.
class No:
    def __init__(self, dado):
         self.dado     = dado;  # Valor Armazenado.
         self.proximo  = None   # Referência ao proximo No.
         self.anterior = None   # Referência ao No anterior.
         
         