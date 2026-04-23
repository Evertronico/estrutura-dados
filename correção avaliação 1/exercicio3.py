# Simulando um vetor de tamanho fixo 10
vetor = [None] * 10
tamanho_atual = 0

def exibir_vetor():
    elementos = [vetor[i] for i in range(tamanho_atual)]
    print(f"Vetor: {elementos} (Tamanho: {tamanho_atual})")

def inserir_posicao(valor, pos):
    global tamanho_atual
    if tamanho_atual >= 10 or pos < 0 or pos > tamanho_atual:
        print("Erro: Posição inválida ou vetor cheio.")
        return

    # Deslocamento para a direita (manual)
    for i in range(tamanho_atual, pos, -1):
        vetor[i] = vetor[i-1]
    
    vetor[pos] = valor
    tamanho_atual += 1

def remover_manual(pos):
    global tamanho_atual
    if pos < 0 or pos >= tamanho_atual:
        print("Erro: Posição inválida.")
        return

    # Deslocamento para a esquerda (manual)
    for i in range(pos, tamanho_atual - 1):
        vetor[i] = vetor[i+1]
    
    vetor[tamanho_atual - 1] = None
    tamanho_atual -= 1

def busca_sequencial(valor):
    for i in range(tamanho_atual):
        if vetor[i] == valor:
            return i
    return -1

# Demonstração
inserir_posicao(10, 0)
inserir_posicao(20, 1)
inserir_posicao(15, 1) # Insere entre o 10 e o 20
exibir_vetor()
remover_manual(1)
exibir_vetor()