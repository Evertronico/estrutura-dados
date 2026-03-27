# Lista que representa a fila de pacientes
fila = []

# -------------------------
# Função para adicionar paciente no final da fila
# -------------------------
def entrar_na_fila(nome):
    # Sempre entra no final (comportamento de fila)
    fila.append(nome)
    print(f"Paciente '{nome}' entrou na fila.")

# -------------------------
# Função para atender paciente (remover do início)
# SEM usar pop(0)
# -------------------------
def atender_paciente():
    # Primeiro, verifica se a fila está vazia
    if len(fila) == 0:
        print("Fila vazia! Nenhum paciente para atender.")
        return
    
    # Guarda o primeiro paciente (quem será atendido)
    paciente_atendido = fila[0]
    
    # Agora vamos deslocar todos os elementos para a esquerda
    for i in range(0, len(fila) - 1):
        fila[i] = fila[i + 1]
    
    # Remove o último elemento duplicado
    fila.pop()
    
    print(f"Paciente '{paciente_atendido}' foi atendido.")

# -------------------------
# Função para exibir a fila
# -------------------------
def mostrar_fila():
    if len(fila) == 0:
        print("Fila vazia.")
        return
    
    print("\n=== FILA DE PACIENTES ===")
    for i in range(len(fila)):
        print(f"{i+1} - {fila[i]}")

# -------------------------
# MENU INTERATIVO
# -------------------------

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar paciente")
    print("2 - Atender paciente")
    print("3 - Mostrar fila")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    # Adicionar paciente
    if opcao == "1":
        nome = input("Nome do paciente: ")
        entrar_na_fila(nome)
    
    # Atender paciente (pode fazer várias vezes → simula atendimentos sequenciais)
    elif opcao == "2":
        atender_paciente()
    
    # Mostrar fila
    elif opcao == "3":
        mostrar_fila()
    
    # Sair
    elif opcao == "0":
        print("Encerrando sistema... 👋")
        break
    
    else:
        print("Opção inválida!")