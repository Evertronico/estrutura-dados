estoque = []

def entrada(nome, qtd):
    for p in estoque:
        if p["nome"] == nome:
            p["qtd"] += qtd
            return
        estoque.append({"nome:": nome, "qtd": qtd})

def saida(nome, qtd):
    for p in estoque:
        if p["nome"] == nome:
            if qtd <= p["qtd"]:
                p["qtd"] -= qtd
            else:
                print("Estoque insuficiente")

def buscar(nome):
    for p in estoque:
        if p["nome"] == nome:
            return p
        return None
    
def listar():
    for p in estoque:
        print(p)