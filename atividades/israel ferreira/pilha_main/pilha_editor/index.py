from pilha_editor import Editor

editor = Editor()

editor.adicionar("Olá, mundo!")
editor.adicionar("Bem-vindo ao editor de texto.")
editor.adicionar("Este e um exemplo de implementação de pilha.")

editor.mostrar()

editor.desfazer()
print("\n--------")

editor.mostrar()