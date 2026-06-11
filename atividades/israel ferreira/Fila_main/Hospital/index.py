from atendimento import AtendimentoHospitalar

hospital = AtendimentoHospitalar()

hospital.chegar_paciente("joão")
hospital.chegar_paciente("maria")
hospital.chegar_paciente("pedro")
hospital.exibir_fila()
hospital.atender_paciente()
hospital.exibir_fila()