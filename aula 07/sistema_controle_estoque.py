produtos = ["mouse", "teclado", "monitor"]
quantidades = [10, 5, 3]

produto_busca = "teclado"

indice = -1

for i in range(len(produtos)):
    if produtos[i] == produto_busca:
        indice = i
        break

if indice != -1:
    print("Produto encontrado.")
    print("Quantidade em estoque:", quantidades[indice])
else:
    print("Produto não encontrado.")