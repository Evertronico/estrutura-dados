
from editor import Editor

# Criar editor
editor = Editor()

# Exemplo de execução
editor.adicionar("Escreveu 'Olá'")
editor.adicionar("Escreveu 'Mundo'")
editor.exibir()

editor.desfazer()
editor.desfazer()
editor.exibir()

editor.refazer()
editor.exibir()

editor.adicionar("Escreveu '!!!'")
editor.exibir()
