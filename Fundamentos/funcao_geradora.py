from time import sleep

def gerador():  # Esta função chama-se função geradora
    for v in range(1000):
        yield v  # yield é a instrução que gera o gerador e retorna os valores sob demanda
        sleep(0.1)

g = gerador()

for value in g:
    print(value)