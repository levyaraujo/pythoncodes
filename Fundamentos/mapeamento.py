from dados import produtos, pessoas, lista

nomes = map(lambda p: f'{p["name"]} - {p["idade"]} anos ', pessoas)

for pessoa in nomes:
    print(pessoa)
