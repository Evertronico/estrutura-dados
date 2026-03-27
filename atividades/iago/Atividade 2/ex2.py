# Atividade 2 - Ex 2: Stock
stock = {
    "Teclado": 15,
    "Rato": 20,
    "Monitor": 10
}

def atualizar_stock(produto, quantidade):
    if produto in stock:
        stock[produto] += quantidade
        print(f"Stock de {produto} atualizado para {stock[produto]}")
    else:
        print("Produto não encontrado.")

# Teste
atualizar_stock("Rato", 5)
print(f"Stock atual: {stock}")