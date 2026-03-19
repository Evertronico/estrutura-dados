def sistema_estoque():
    estoque = []

    def adicionar_produto(nome, qtd):
        for produto in estoque:
            if produto['nome'].lower() == nome.lower():
                produto['qtd'] += qtd
                print(f"Quantidade de '{nome}' atualizada para {produto['qtd']}.")
                return
        estoque.append({'nome': nome, 'qtd': qtd})
        print(f"Produto '{nome}' adicionado com sucesso.")

    def saida_produto(nome, qtd):
        for produto in estoque:
            if produto['nome'].lower() == nome.lower():
                if produto['qtd'] >= qtd:
                    produto['qtd'] -= qtd
                    print(f"Saída de {qtd} unidade(s) de '{nome}' realizada.")
                else:
                    print(f"Erro: Estoque insuficiente para '{nome}'. Disponível: {produto['qtd']}.")
                return
        print("Erro: Produto não encontrado.")

    def buscar_produto(nome):
        for produto in estoque:
            if produto['nome'].lower() == nome.lower():
                print(f"Produto encontrado: {produto['nome']} - Quantidade: {produto['qtd']}")
                return
        print("Produto não encontrado.")

    def exibir_estoque():
        print("\n--- Estoque Atual ---")
        if not estoque:
            print("O estoque está vazio.")
        else:
            for produto in estoque:
                print(f"-> {produto['nome']}: {produto['qtd']} unidades")

    adicionar_produto("Teclado", 10)
    adicionar_produto("Mouse", 5)
    adicionar_produto("Teclado", 5) 
    exibir_estoque()
    
    saida_produto("Mouse", 2)
    saida_produto("Mouse", 10)
    buscar_produto("Teclado")
    exibir_estoque()

sistema_estoque()