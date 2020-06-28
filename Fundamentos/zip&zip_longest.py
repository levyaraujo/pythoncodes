from itertools import zip_longest, count

index = count()
cidades = ['Rio de Janeiro', 'Nova York', 'Columbus', 'Toronto', 'Paris']
estados = ['RJ', 'NY', 'OH']

cidades_e_estados = zip(
    index,
    estados,
    cidades
)
for valor in cidades_e_estados:
    print(*valor)
