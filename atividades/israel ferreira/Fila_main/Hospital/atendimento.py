class AtendimentoHospitalar:
    def __init__(self):
        
        # fila de pacientes
        self.fila = []
        
        
    # chega um paciente 
    def chegar_paciente(self, nome):
        self.fila.append(nome)
        print(f"Paciente {nome} entrou na fila.")
    
    # atendimento do paciente
    def atender_paciente(self):
        if len(self.fila) == 0:
            print("nenhum paciente aguardando")
            return
        paciente = self.fila.pop(0)
        print(f"Paciente {paciente} foi atendido.")
            
    # exibir a fila de pacientes
    def exibir_fila(self):
        if len(self.fila) == 0:
            print("nenhum paciente aguardando")
            return
        print("fila de pacientes:")
        for paciente in self.fila:
                print(f"- {paciente}")