class Solicitacao:
    def __init__(
        self,
        id,
        paciente,
        tipo,
        gravidade,
        urgencia,
        tempo_espera):
        self.id = id
        self.paciente = paciente
        self.tipo = tipo
        self.gravidade = gravidade
        self.urgencia = urgencia
        self.tempo_espera = tempo_espera
        
    def prioridade(self):
        return(
            self.gravidade * 5 +
            self.urgencia * 3 +
            self.tempo_espera 
            )
    
    def __str__(self):
        return (f"ID {self.id} |"
                f"Paciente: {self.paciente} |"
                f"Tipo: {self.tipo} |"
                f"Gravidade: {self.gravidade} |"
                f"Urgencia: {self.urgencia} |"
                f"Espera: {self.tempo_espera} dias |"
                f"Score: {self.prioridade()} |")
    