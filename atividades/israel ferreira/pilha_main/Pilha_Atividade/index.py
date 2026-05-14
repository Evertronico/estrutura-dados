"""
    Evolua o sistema de editor implementando suporte completo às operações de 
    desfazer Undo e refazer Redo. O sistema deverá utilizar duas pilhas 
    independentes para controlar o histórico de ações realizadas e as ações desfeitas.
    Requisitos:
        ● Implementar uma pilha undo
        ● Implementar uma pilha redo
        ● Adicionar novas ações ao sistema
        ● Desfazer ações utilizando a pilha undo
        ● Refazer ações utilizando a pilha redo
        ● Limpar a pilha redo quando uma nova ação for adicionada
        ● Exibir o estado atual do histórico
"""
from Pilha_Atividade import Editor
from Pilha_Atividade import Pilha

# Criar editor
editor = Editor()

# Exemplo de execução
editor.nova_acao("Escreveu 'Olá'")
editor.nova_acao("Escreveu 'Mundo'")
editor.mostrar_historico()

editor.desfazer()
editor.mostrar_historico()

editor.refazer()
editor.mostrar_historico()

editor.nova_acao("Escreveu '!!!'")
editor.mostrar_historico()
