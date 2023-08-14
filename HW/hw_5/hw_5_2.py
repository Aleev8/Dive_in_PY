# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# Вывод:
# {'Vlad': 102.5, 'Den': 300.0, 'Alex': 600.0}

def dict_of_awards(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: money / 100 * perc
            for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}


# Ввод:
name_list = ['Vlad', 'Den', 'Alex', 'Barby', 'Ken', 'Oppenheimer']
salary_list = [1000, 2000, 3000, 5000, 6000, 10000]
extra_list = ['10.25%', '15%', '20%', '30%', '33%', '55%']

print(dict_of_awards(name_list, salary_list, extra_list))