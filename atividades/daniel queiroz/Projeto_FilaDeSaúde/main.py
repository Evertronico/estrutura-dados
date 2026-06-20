# =====================================================================
# SISTEMA DE FILA DE SAÚDE - Projeto de Estrutura de Dados
# Aluno: Daniel Queiroz
#
# Atendimento por prioridade (fila de prioridade). O score combina
# gravidade, urgência (com peso) e tempo de espera.
# Para executar, dentro da pasta "Projeto_FilaDeSaúde", rode:
#       python main.py
# =====================================================================

import random
from datetime import date, timedelta

from paciente import Paciente
from fila_saude import FilaSaude

NOMES = ["Ana Costa", "Carlos Mendes", "Maria Souza", "Fernanda Rocha",
         "João Silva", "Pedro Lima", "Ricardo Alves", "Juliana Martins",
         "Patrícia Gomes", "Lucas Oliveira"]

TIPOS = ["CONSULTA", "EXAME", "MEDICAMENTO"]


# Gera uma fila nova com pacientes aleatórios
def gerar_fila(quantidade=15):
    fila = FilaSaude()
    for i in range(quantidade):
        id_paciente = 101 + i
        nome = random.choice(NOMES)
        tipo = random.choice(TIPOS)
        gravidade = random.randint(1, 5)
        urgencia = random.randint(1, 5)
        dias = random.randint(1, 120)
        data_entrada = date.today() - timedelta(days=dias)
        fila.enfileirar(Paciente(id_paciente, nome, tipo, gravidade, urgencia, data_entrada))
    return fila


def main():
    fila = gerar_fila()

    while True:
        print("\n==============================")
        print(" SISTEMA DE FILA DE SAÚDE")
        print("==============================")
        print("1 - Exibir fila")
        print("2 - Atender próximo")
        print("3 - Recarregar fila")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            fila.exibir()
        elif opcao == "2":
            paciente = fila.atender_proximo()
            if paciente is None:
                print("\nNão há pacientes na fila.")
            else:
                print(f"\nAtendendo agora: {paciente}")
        elif opcao == "3":
            fila = gerar_fila()
            print("\nFila recarregada com novos pacientes.")
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
