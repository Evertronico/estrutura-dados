# Atividade 2 - Ex 4: Vendas
vendas = [1200, 800, 2500, 1500, 3000]

soma = 0
for v in vendas:
    soma += v
media = soma / len(vendas)

acima_media = []
for v in vendas:
    if v > media:
        acima_media[:] = acima_media + [v]

print(f"Média de vendas: {media:.2f}")
print(f"Vendas acima da média: {acima_media}")