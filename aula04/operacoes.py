def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def media(n1,n2):
    return (n1 + n2) /2 

def aprovacao(nome_aluno, nome_curso, nota1, nota2):
    media_c = media(nota1, nota2)

    situacao = "Aprovado" if media_c >= 6 else "Reprovado"
    
    return (
        f"O aluno {nome_aluno} matriculado no curso {nome_curso} "
        f"está {situacao} (média: {media_c:.1f})."
    )


