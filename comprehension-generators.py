# Se a variável generator fosse delimitada por colchetes (como uma lista),
# ela seria uma list comprehension normal e não um gerador

generator = (g for g in range(1000))  # Cria um objeto gerador usando "tuple comprehension"

for value in generator:  # Retorna os valores sob demanda, como o yield
    print(value)

print(type(generator)) # Retorna o tipo da variável, para não restar dúvidas