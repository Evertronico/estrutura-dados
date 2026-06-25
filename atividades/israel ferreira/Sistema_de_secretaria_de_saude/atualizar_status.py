from banco import conectar

def concluir_solicitacao(id_solicitacao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE solicitacoes
        SET status = 'CONCLUIDO'
        WHERE id = %s
    """, (id_solicitacao,))
    
    conexao.commit()
    conexao.close()