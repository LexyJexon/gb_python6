'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''


def find_indexes(arr, min, max):
    res = []
    for a in arr:
        if min <= a <= max:
            res.append(a)
    return res


if __name__ == '__main__':
    max = int(input("Введите верхний предел диапазона: "))
    min = int(input("Введите верхний нижний диапазона: "))
    n = int(input("Введите количество элементов массива: "))
    arr = [int(input("Введите элемент массива: ")) for i in range(0, n)]
    print(find_indexes(arr, min, max))
