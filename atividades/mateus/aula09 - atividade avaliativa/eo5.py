# Exercício 5 – Sistema de Atendimento com Fila
# Implemente um sistema de atendimento para um consultório utilizando lista para simular uma fila de pacientes.
# Requisitos:
#  * Inserir pacientes no final da lista
#  * Remover paciente do início da lista manualmente (sem pop(0))
#  * Implementar função para exibir fila
#  * Controlar caso de fila vazia
#  * Simular múltiplos atendimentos sequenciais

def inserir(lista, valor):
    lista.append(valor);

def remover(lista):
    if len(lista) == 0:
        print('A lista está vazia')
        return
    
    for i in range(0, len(lista)-1):
        lista[i] = lista[i+1]
    lista.pop()

def exibir(lista):
    for valor in lista:
       print(valor)

fila = []
cont = 0

while (cont <= 5):
    inserir(fila,f'paciente{cont}')
    cont+=1

exibir(fila)
print('='*30)

remover(fila)

print('='*30)
exibir(fila)
