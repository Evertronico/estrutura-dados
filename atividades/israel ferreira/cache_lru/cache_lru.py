# importa a classe no
from no import No #primeiro o nomde depois a classe

# classe de cache LRU
class CacheLRU:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        
        # estrutura auxiliar para acesso rápido
        self.cache = {}
        
        # ponteiro para a lista duplamente encadeada
        self.head = None
        self.tail = None
    
    # incluir um item no inicio da lista
    def _adicionar_no_inicio(self, no):
        no.proximo = self.head
        no.anterior = None
        
        if self.head:
            self.head.anterior = no
            
        self.head = no
        
        if self.tail is None:
            self.tail = no
    
    # remove o nó da lista
    def _remover_no(self, no):
        if no.anterior:
            no.anterior.proximo = no.proximo
        else:
            self.head = no.proximo
        
        if no.proximo:
            no.proximo.anterior = no.anterior
        else:
            self.tail = no.anterior
    
    # move um item para o inicio da lista
    def _mover_para_inicio(self, no):
        self._remover_no(no)
        self._adicionar_no_inicio(no)
        
    # recupera um item do cache
    def get(self, chave):
        # caso o item não exista
        if chave not in self.cache:
            return None
        
        no = self.cache[chave]
        
        # move para o mais recente
        self._mover_para_inicio(no)
        
        return no.valor
    
    # adiciona um item ao cache
    def put(self, chave, valor):
        # se o item já existe , atualiza o valor e move para o inicio
        if chave in self.cache:
            no = self.cache[chave]
            no.valor = valor
            self._mover_para_inicio(no)
            return
        # cria um novo nó
        novo = No(chave, valor)
        # adiciona no inicio
        self._adicionar_no_inicio(novo)
        # adiciona ao dicionário
        self.cache[chave] = novo
        
        # verrifica se exedeu a capacidade
        if len(self.cache) > self.capacidade:
            # removeo item menos usado
            chave_remover = self.tail.chave
            self._remover_no(self.tail)
            
            del self.cache[chave_remover]
            
    def exibir(self):
        atual = self.head
        
        print("Cache (mais recente -> menos recente):")
        
        while atual:
            print(f"{atual.chave}: {atual.valor}")
            atual = atual.proximo