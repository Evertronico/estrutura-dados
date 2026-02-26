def some(a, b):
    return a + b

def multiplique(a, b):
    return a * b

def exponencie(a, b):
    return a ** b

def calcule_media(n1, n2):
    return (n1 + n2) / 2

def valide_aprovacao(media):
    if media >= 6:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
def exiba_result_aluno(nome, curso, nota1, nota2):
    media = calcule_media(nota1, nota2)
    situacao = valide_aprovacao(media)

    return f'{nome} matriculado no curso {curso} está {situacao}'