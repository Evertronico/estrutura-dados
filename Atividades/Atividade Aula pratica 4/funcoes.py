def verificar_aprovacao(nome, curso, nota1, nota2):
    media = (nota1 + nota2) / 2
    
    if media >= 6:
        status = "Aprovado"
    else:
        status = "Reprovado"
    
    return f"{nome} matriculado no curso {curso} está {status}."