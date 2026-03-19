# Leitura de um dado numérico fornecido pelo usuário
# O valor representa um dado bruto que será analisado pelo algoritmo
nota = float(input("Digite a nota do aluno: "))

# Estrutura condicional responsável pela tomada de decisão
# O if avalia uma condição lógica baseada no dado informado
if nota >= 6:
    # Execução deste bloco ocorre quando a condição é verdadeira
    print("Aluno aprovado")  # Informação gerada a partir do dado
else:
    # Execução alternativa quando a condição é falsa
    print("Aluno reprovado")  # Informação resultante da análise lógica
