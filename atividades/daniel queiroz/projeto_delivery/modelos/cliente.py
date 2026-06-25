# Modelo do Cliente
# Representa um cliente cadastrado no sistema de delivery.

class Cliente:
    def __init__(self, id_cliente, nome, telefone, endereco):
        self.id = id_cliente         
        self.nome = nome              
        self.telefone = telefone     
        self.endereco = endereco      

    def __str__(self):
        return f"[{self.id}] {self.nome} | Tel: {self.telefone} | Endereço: {self.endereco}"
