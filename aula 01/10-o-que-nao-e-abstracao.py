# código repetido não é abstração
media1 = (6 + 8 + 7) / 3
media2 = (5 + 9 + 8) / 3

# isso é abstração
def media(notas):
    return sum(notas) / len(notas)

print(media([6, 8, 7]))
print(media([5, 9, 8]))
