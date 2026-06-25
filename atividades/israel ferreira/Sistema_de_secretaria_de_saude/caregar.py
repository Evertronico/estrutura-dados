from banco import conectar
from solicitacao import Solicitacao

def carregar_solicitacoes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT 
            s.id, p.nome, s.tipo, s.gravidade, s.urgencia, DATEDIFF(CURDATE(), DATE(s.data_solicitacao)) AS tempo_espera
        FROM solicitacoes s
        INNER JOIN pacientes p ON  p.id = s.paciente_id 
        WHERE s.status = 'AGUARDANDO'
    """)
    
    resultado = cursor.fetchall()
    
    print(f"\nRegistros encontrados: {len(resultado)}\n")
    dados = []

    for linha in resultado:
        dados.append(
            Solicitacao(
                linha[0],
                linha[1],
                linha[2],
                linha[3],
                linha[4],
                linha[5]
        )
    )
    conexao.close()
    return dados
