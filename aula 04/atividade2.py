import atividadeoperacoes

nome, curso, nota1, nota2 = atividadeoperacoes.receba_dados()
print(atividadeoperacoes.valide_aprovacao(atividadeoperacoes.calcule_media(nota1, nota2)))
