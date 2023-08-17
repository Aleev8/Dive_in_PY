# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# и возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь. Проверку года на високосность вынести в
# отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

def check_date(date: str):
    dd, mm, yy = map(int, date.split('.'))
    print (dd, mm, yy)
    if 1 <= yy <= 9999:
        if mm in [1, 3, 5, 7, 8, 10, 12] and 1 <= dd <= 31:
            return True
        elif mm in [4, 6, 9, 11] and 1 <= dd <= 30:
            return True
        elif 1 <= dd <= 28 + check_leap_year(yy):
            return True
        else:
            return False
    return False


def check_leap_year(yy):
    return yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0

def calend_tetminal():
    date = argv[1]
    print(check_date(date))