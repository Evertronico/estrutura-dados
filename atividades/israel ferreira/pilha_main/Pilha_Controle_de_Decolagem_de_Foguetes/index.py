
from controle import ControleLancamento


controle = ControleLancamento()


controle.adicionar("Iniciar contagem regressiva")
controle.adicionar("Ativar sistemas de navegação")
controle.adicionar("Pressurizar tanques de combustível")
controle.adicionar("Acionar motores principais")
controle.adicionar("Liberar torre de lançamento")
controle.adicionar("Decolar")

controle.exibir()

controle.desfazer()
controle.desfazer()
controle.exibir()

controle.refazer()
controle.exibir()

controle.adicionar("Separação do primeiro estágio")
controle.exibir()

