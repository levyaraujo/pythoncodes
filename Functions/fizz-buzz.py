def fizzbuzz(num):
    # Se o parâmetro num for divisivel por 3 e 5 (15): retorna a string 'FizzBuzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


validação = fizzbuzz(30)
print(validação)
