transacoes = [120.50, -50.00, 200.00, -30.25, 75.00, -10.00]

saldo = 0

for valor in transacoes:
    #cadaa transacao modifica meu saldo de maneira acumulativa
    saldo += valor

print("Transacoes: ", transacoes)
print("Saldo total: R$", saldo)