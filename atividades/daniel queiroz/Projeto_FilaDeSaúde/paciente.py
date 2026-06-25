# Modelo: PACIENTE
from datetime import date

# Pesos usados no cálculo da prioridade (score)
PESO_GRAVIDADE = 5
PESO_URGENCIA = 3
PESO_ESPERA = 1


class Paciente:
    def __init__(self, id_paciente, nome, tipo, gravidade, urgencia, data_entrada):
        self.id = id_paciente
        self.nome = nome
        self.tipo = tipo                # CONSULTA, EXAME ou MEDICAMENTO
        self.gravidade = gravidade      # 1 a 5
        self.urgencia = urgencia        # 1 a 5
        self.data_entrada = data_entrada

    # Quantos dias o paciente está esperando
    def dias_espera(self):
        return (date.today() - self.data_entrada).days

    # Prioridade final: quanto maior o score, mais cedo é atendido
    def score(self):
        return (self.gravidade * PESO_GRAVIDADE
                + self.urgencia * PESO_URGENCIA
                + self.dias_espera() * PESO_ESPERA)

    def __str__(self):
        return (f"ID:{self.id} | Paciente:{self.nome} | Tipo:{self.tipo} | "
                f"Gravidade:{self.gravidade} | Urgência:{self.urgencia} | "
                f"Espera:{self.dias_espera()} dias | Score:{self.score()}")
