import math


def helloer(name):
    print(f'Hello {name}!!!')


def print_line(n):
    print('-' * n)


def nastennaia_nadpis(name1, name2):
    print(f"{name1} + {name2} = любов")


def summ(a, b):
    result = a + b
    return result


def calculator(n1, n2, sign):
    if sign == '+':
        return n1 + n2
    elif sign == '-':
        return n1 - n2
    elif sign == '*':
        return n1 * n2
    elif sign == '/':
        return n1 / n2
    elif sign == '$':
        return (n1 + n2) * (n1 - n2)
    elif sign == '^':
        result = 1
        i = 0
        while i < n2:
            result = result * n1
            i += 1
        return result


def find_P(radius):
    return 2 * math.pi * radius


def find_S(radius):
    return math.pi * calculator(radius, 2, '^')


def find_cylinder_V(radius, h):
    return find_S(radius) * h


def filter_names_list(names, letter):
    new_names = []
    for name in names:
        if letter in name.lower():
            new_names.append(name)
    return new_names


def find_sum_of_numbers(numbers):
    """
    :param numbers: list - список чисел
    :return: int - сумма всіх чисел у списку
    """
    s = 0
    for number in numbers:
        s += number
    return s


def mnozh(symbol, n=30):
    """
    :param symbol: str - символ, який треба розмножити
    :param n: int - на скільки треба розмножити
    :return: str - розмножений символ
    """
    return symbol * n


def my_range(a, b=None, step=1):
    if b is None:
        stop = a
        start = 0
    else:
        start = a
        stop = b
    rng = []
    while start < stop:
        rng.append(start)
        start += step
    return rng


def skleivatel(sym, *strings):
    """
    :sym: символ, через який ми будемо склеювати строки
    :strings: строки, які ми хочемо склеїти

    Приклад:
    skleivatel('+', 'Bob', 'Alya', 'Asya', 'Vasya') -> 'Bob+Alya+Asya+Vasya'
    skleivatel('+', 'Bob', 'Alya') -> 'Bob+Alya'
    :return:
    """
    text = ''
    for word in strings:
        text += word + sym
    return text[:-len(sym)]



