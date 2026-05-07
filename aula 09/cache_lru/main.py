from cache import CacheLRU

cache = CacheLRU(3)

cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)

cache.exibir()

print("\nAcessando B...")
cache.get("B")

cache.exibir()

print("\nInserindo D (remove o menos usado)...")
cache.put("D", 4)

cache.exibir()