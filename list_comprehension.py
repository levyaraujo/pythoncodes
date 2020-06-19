string = '01234567890123456789012345678901234567890123456789'

lista = [string[x: x+10] for x in range(0, len(string), 10)]
base = '.'.join(lista)

print(base)
