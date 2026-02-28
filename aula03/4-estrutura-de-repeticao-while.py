# Variável de controle inicial do laço
contador = 0

# Laço while executa enquanto a condição lógica for verdadeira
# O número de repetições não é conhecido previamente
while contador < 3:
    # Execução repetida do bloco enquanto a condição for satisfeita
    print("Contador:", contador)  # Informação exibida a cada iteração

    # Atualização da variável de controle
    # Evita laço infinito e garante o término do algoritmo
    contador += 1
