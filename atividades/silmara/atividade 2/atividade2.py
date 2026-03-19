# Exercício 2 – Controle de Estoque com Validação de Regras
# Implemente um sistema de controle de estoque para uma loja. Cada produto deve possuir nome e quantidade disponível.
# Requisitos:
# Utilizar lista de estruturas (dicionário ou lista composta)
#  * Implementar entrada de produto (adicionar ou atualizar quantidade)
#  * Implementar saída de produto com validação de estoque
#  * Impedir retirada maior que a quantidade disponível
#  * Implementar busca de produto pelo nome
#  * Exibir todos os produtos

estoque = []

def gerenciar_produto(nome, quantidade):
    for produto in estoque:
        if produto['nome'] == nome:
            produto['quantidade'] += quantidade
            return
    estoque.append({'nome': nome, 'quantidade': quantidade})

def saida_produto(nome, qtd_saida):
    for produto in estoque:
        if produto['nome'] == nome:
            if produto['quantidade'] >= qtd_saida:
                produto['quantidade'] -= qtd_saida
                print("Saída realizada.")
            else:
                print("Estoque insuficiente!")
            return
    print("Produto não encontrado.")

def mostrar_estoque():
    print("----------")
    for produto in estoque:
        print(f"Produto: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")

gerenciar_produto('Saco de milho', 2)
gerenciar_produto('Ração pra cachorro', 5)

# saida_produto('Batatas', 45)
saida_produto('Saco de milho', 45)
mostrar_estoque()

saida_produto('Saco de milho', 1)
mostrar_estoque()
