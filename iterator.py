numbers = [1, 2, 4, 5, 6, 7, 8]

iterator = iter(numbers)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

print(type(iterator))
