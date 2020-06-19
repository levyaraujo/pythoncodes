from time import sleep

def gerador():  # Esta função chama-se função geradora
    for v in range(1000):
        yield v  # yield é a instrução que carrega na memória e retorna um valor por vez
        sleep(0.1)

g = gerador()

for value in g:
    print(value)