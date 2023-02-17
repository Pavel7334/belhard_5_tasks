"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""
import collections


def common_and_longest(text: str) -> tuple:

    words = text.split()
    counter = collections.Counter(words)
    # most_common, occurrences = counter.most_common()[0]     #РАСПАКОВКА TUPLE
    most_common = counter.most_common()[0]
    longest = max(words, key=len)
    return most_common[0], longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
