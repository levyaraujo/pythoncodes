from random import randint

cpf = str(randint(100000000, 999999999))
novo_cpf = cpf
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        novo_cpf += str(digito)


def sep_cpf(numero):
    temp = [numero[x: x+3] for x in range(0, 9, 3)]
    base = '.'.join(temp)
    digit = numero[- (len(numero) % 3):]
    return base + '-' + digit


print(sep_cpf(novo_cpf))
