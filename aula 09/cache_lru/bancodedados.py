import time
from cache import CacheLRU

# simulação de um banco de dados
class BancoDeDadosSimulado:
    def __init__(self):
        # simula uma tabela de usuários
        self.dados = {
            "user_1": {
                "nome": "Alice", 
                "email": "alice@example.com", 
                "plano": "premium"
            },
            "user_2": {
                "nome": "Bob", 
                "email": "bob@example.com", 
                "plano": "basic"
            },
            "user_3": {
                "nome": "Charlie", 
                "email": "charlie@example.com", 
                "plano": "premium"
            },
            "user_4": {
                "nome": "David", 
                "email": "david@example.com", 
                "plano": "basic"
            },
            "user_5": {
                "nome": "Eve", 
                "email": "eve@example.com", 
                "plano": "premium"
            },
            "user_6": {
                "nome": "Frank", 
                "email": "frank@example.com", 
                "plano": "basic"
            },
            "user_7": {
                "nome": "Grace", 
                "email": "grace@example.com", 
                "plano": "premium"
            },
        }

    def buscar_no_disco(self, user_id):
        print(f"[DB] consultando {user_id} no banco de dados... (aguarde)")
        time.sleep(1.5)
        return self.dados.get(user_id, None)
    
# servico que gerencia a lógica do negocio
class UserService:
    def __init__(self, capacidade_cache):
        self.db = BancoDeDadosSimulado()
        self.cache = CacheLRU(capacidade_cache)

    def obter_perfil(self, user_id):
        start_time = time.time()

        # primeiro tenta obter do cache
        perfil = self.cache.get(user_id)

        if perfil:
            origem = "CACHE (HIT)"
        else:
            # nao encontrou no cache, busca no banco de dados
            perfil = self.db.buscar_no_disco(user_id)
            origem = "DISCO (MISS)"

            # se o dado existe armazena no cache
            if perfil:
                self.cache.put(user_id, perfil)
            
        duracao = time.time() - start_time

        # exibe o resultado de forma visual
        print(f"Resultado: {perfil} (origem: {origem}, tempo: {duracao:.2f} segundos)")
        print("-" * 50)
        return perfil
        
# execucao do cenario de teste
if __name__ == "__main__":
    # cria um servico limitando a memória a apenas 3 usuários
    service = UserService(capacidade_cache=10)

    print("1 rodada de consulta (todos MISS - cache vazio):")
    # cada uma dessas chamadas vai durar 1.5s
    service.obter_perfil("user_1")
    service.obter_perfil("user_2")
    service.obter_perfil("user_3")

    print("\n2 rodada de consulta - acesso repetido (HIT - instantâneo):")
    service.obter_perfil("user_1")

    print("\n3 rodada de consulta - insere um novo e expulsa o menos acessado:")
    service.obter_perfil("user_4")

    print("\n4 rodada de consulta - provando que user_2 foi expulso")
    service.obter_perfil("user_2")

    print("\nEstado final da memória cache:")
    service.cache.exibir()