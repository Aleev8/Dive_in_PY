# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
#
# Чтобы записать байты можно использовать список с числами и функцию bytes
#


from random import choices, randint
from string import ascii_letters, digits


def create_files(extension: str, min_name: int = 6, max_name: int = 30,
                 min_byte: int = 256, max_byte: int = 4096, many_files: int = 42):
    for _ in range(many_files):
        name = ''.join(choices(ascii_letters + digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_byte, max_byte)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

print(create_files('txt', 2))