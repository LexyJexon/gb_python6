'''
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''


def generate_arr(first, diff, n):
    arr = [first]
    for i in range(1, n):
        arr.append(arr[i-1] + (n-i) * diff)
    return arr


if __name__ == '__main__':
    first = int(input("Введите первый элемент арфиметической прогрессии: "))
    n = int(input("Введите количество элементов прогрессии: "))
    diff = int(input("Введите разность прогресии: "))
    print(generate_arr(first, diff, n))


