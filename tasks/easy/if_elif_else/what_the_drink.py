"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Какой напиток можно взять?

* детям (до 14 лет) можно сок
* подросткам (до 18 лет) можно кока-колу
* от 18 до 21 года можно пиво
* тем, кто старше 21 можно виски

Отредактировать функцию what_you_drink, которая принимает возраст таким образом,
чтобы она возвращала напиток

ПРИМЕРЫ
--------------------------------------------------------------------------------
what_you_drink(13) == "можно сок"
what_you_drink(17) == "можно кока-колу"
what_you_drink(18) == "можно пиво"
what_you_drink(20) == "можно пиво"
what_you_drink(30) == "можно виски"
"""


def what_you_drink(age: int) -> str:
    if age <= 14:
        return "можно сок"
    if 14 <= age <= 17:
        return "можно кока-колу"
    if 18 <= age <= 20:
        return "можно пиво"
    if age >= 21:
        return "можно виски"

if __name__ == '__main__':
    age_val = int(input('Введите возраст: '))
    print(f'Напиток: {what_you_drink(age_val)}')
