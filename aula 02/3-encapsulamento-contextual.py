# Função que cria um TDA com encapsulamento
def criar_tda_alunos():
    # Estrutura interna protegida
    alunos = []

    # Operação que permite adicionar alunos ao TDA
    # O acesso direto à lista não é permitido
    def adicionar(nome):
        alunos.append(nome)

    # Operação que permite consultar os dados do TDA
    # Retorna uma cópia para preservar o encapsulamento
    def listar():
        return alunos.copy()

    # Retorno das operações que definem a interface do TDA
    return adicionar, listar

# Criação do TDA e obtenção das operações disponíveis
adicionar, listar = criar_tda_alunos()

# Uso do TDA sem acesso direto à estrutura interna
adicionar("Ana")
adicionar("Bruno")

# Consulta aos dados por meio da operação definida
print(listar())
