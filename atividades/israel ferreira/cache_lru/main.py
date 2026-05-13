from cache_lru import CacheLRU

# teste do cache lru
cache = CacheLRU(3)

# adiciona item ao cache
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)

# exibe a lista de itens
cache.exibir()

print("acessando B...")
cache.get('b')
cache.exibir()

# insere um novo item
print("inserindo D... (remove o menos usado)")
cache.put('d', 4)
cache.exibir()