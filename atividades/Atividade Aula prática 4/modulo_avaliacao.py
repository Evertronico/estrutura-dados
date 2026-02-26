def avaliar_aluno(nome, curso, nota1, nota2):
    media = (nota1 + nota2) / 2
    
    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        
    return f"O aluno {nome} matriculado no curso {curso} está {situacao}"