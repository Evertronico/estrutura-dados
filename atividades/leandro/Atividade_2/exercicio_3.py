# Lista que será mantida SEMPRE ordenada
numeros = []

# Função para inserir mantendo ordem crescente
def inserir_ordenado(lista, valor):
    # Caso 1: lista vazia → só adiciona
    if len(lista) == 0:
        lista.append(valor)
        return
    
    # Primeiro, vamos encontrar a posição correta manualmente
    posicao = 0
    
    for i in range(len(lista)):
        # Quando encontrar um número maior que o valor, achamos a posição
        if valor < lista[i]:
            posicao = i
            break
        posicao = i + 1  # continua avançando
    
    # Agora vamos abrir espaço na lista (simulando deslocamento)
    lista.append(0)  # adiciona um espaço no final
    
    # Desloca os elementos para a direita
    for i in range(len(lista) - 1, posicao, -1):
        lista[i] = lista[i - 1]
    
    # Insere o valor na posição correta
    lista[posicao] = valor


# Função só para exibir a lista
def mostrar_lista(lista):
    print("Lista ordenada:", lista)


# -------------------------
# Testando
# -------------------------

inserir_ordenado(numeros, 5)
inserir_ordenado(numeros, 2)
inserir_ordenado(numeros, 8)
inserir_ordenado(numeros, 1)
inserir_ordenado(numeros, 6)

mostrar_lista(numeros)