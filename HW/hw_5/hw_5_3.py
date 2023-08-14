# Создайте функцию генератор чисел Фибоначчи
import random

def fibonacci(n):
    n1, n2 = 1, 1
    print(n1, n2, end=" " )
    for i in range(n + 1):
        yield n1+n2
        n1, n2 = n2, n1+n2


number = random.randint(5, 30)
print(*fibonacci(number))


