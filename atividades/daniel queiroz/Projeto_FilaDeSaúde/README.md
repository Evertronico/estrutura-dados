# Sistema de Fila de Saúde

Atividade avaliativa **Estrutura de Dados**.
Aluno: **Daniel Queiroz**

Simula o atendimento de pacientes em um posto de saúde usando uma **fila de
prioridade**: quem tem maior necessidade (combinando gravidade, urgência e
tempo de espera) é atendido primeiro.

---

## Estrutura de dados utilizada

**Fila de prioridade.** Diferente de uma fila comum (FIFO, primeiro a chegar é
o primeiro a sair), aqui o paciente é inserido já na posição correta de acordo
com o seu *score* de prioridade. O início da fila é sempre o paciente mais
prioritário.

| Operação          | O que cada um faz                                    | Big O (Temporal)|
|-------------------|------------------------------------------------------|-------|
| `enfileirar`      | Insere o paciente mantendo a ordem por score         | O(n)  |
| `atender_proximo` | Remove e retorna o paciente de maior prioridade      | O(n)  |
| `primeiro`        | Mostra o próximo a ser atendido sem remover          | O(1)  |
| `esta_vazia`      | Verifica se há pacientes na fila                      | O(1)  |
| `tamanho`         | Quantidade de pacientes                              | O(1)  |
| `exibir`          | Lista todos os pacientes com a posição               | O(n)  |

---

## Cálculo da prioridade (score)

Cada paciente recebe um **score**. Quanto maior, mais cedo é atendido:

```
score = gravidade * 5 + urgência * 3 + dias_espera * 1
```

Os pesos ficam como constantes em `paciente.py` e podem ser ajustados:

| Fator        | Constante         | Peso | Faixa        |
|--------------|-------------------|------|--------------|
| Gravidade    | `PESO_GRAVIDADE`  | 5    | 1 a 5        |
| Urgência     | `PESO_URGENCIA`   | 3    | 1 a 5        |
| Dias espera  | `PESO_ESPERA`     | 1    | calculado    |

> O **peso da urgência** é o multiplicador que controla o quanto ela influencia
> a ordem da fila. Basta alterar a constante para mudar a regra de prioridade.

**Exemplo:** paciente com gravidade 5, urgência 4 e 109 dias de espera:

```
5*5 + 4*3 + 109*1 = 25 + 12 + 109 = 146
```

---

## Arquivos do projeto

| Arquivo          | Responsabilidade                                          |
|------------------|----------------------------------------------------------|
| `paciente.py`    | Modelo `Paciente` e o cálculo do score                   |
| `fila_saude.py`  | Estrutura `FilaSaude` (a fila de prioridade)             |
| `main.py`        | Menu do sistema e geração dos pacientes                  |

---

## Como executar

Dentro da pasta `Projeto_FilaDeSaúde`:

```bash
python main.py
```

---

## Menu do sistema

```
==============================
 SISTEMA DE FILA DE SAÚDE
==============================
1 - Exibir fila
2 - Atender próximo
3 - Recarregar fila
0 - Sair
```

| Opção | Ação                                                            |
|-------|-----------------------------------------------------------------|
| 1     | Lista todos os pacientes em ordem de prioridade                 |
| 2     | Atende (remove) o paciente de maior score                       |
| 3     | Gera uma nova fila com pacientes aleatórios                     |
| 0     | Encerra o programa                                              |

---

## Exemplo de saída

```
===== FILA ATUAL =====

1º -> ID:101 | Paciente:Patrícia Gomes | Tipo:EXAME | Gravidade:5 | Urgência:4 | Espera:106 dias | Score:143
2º -> ID:113 | Paciente:Lucas Oliveira | Tipo:MEDICAMENTO | Gravidade:4 | Urgência:5 | Espera:97 dias | Score:132
3º -> ID:103 | Paciente:Fernanda Rocha | Tipo:CONSULTA | Gravidade:5 | Urgência:1 | Espera:83 dias | Score:111
```

---

## Possíveis melhorias

- Cadastrar pacientes manualmente pelo menu.(Backlog)
- Relatório com a contagem de atendimentos por tipo (consulta, exame, medicamento).(Backlog)
- Salvar e carregar a fila a partir de um arquivo.(Backlog)
