def fibonacci(n):
    a, b = 0, 1
    while a < n:  # Enquanto a for menor que n, execute o código abaixo:
        print(a, end='-')
        a, b = b, a + b


fibonacci(145)
