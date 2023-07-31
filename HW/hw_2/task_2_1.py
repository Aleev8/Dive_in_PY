# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

import random

def my_hex(number: int) -> str:
    HEX = 16
    result = ''
    chars_hex = list('0123456789abcdef')
    while number > 0:
        result = chars_hex[number % HEX] + result
        number //= HEX
    return '0x' + result

number = random.randint(1, 100000)

print(f"Случайно сгенерированное число: {number}\n"
      f"Это число в шестнадцитиричной системе счисления: {my_hex(number)}\n"
      f"Проверка через hex: {hex(number)}")
