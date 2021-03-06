'''
A fixed point in an array is an element whose value is equal to its index.
Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
For example, given [-6, 0, 2, 40], you should return 2.
Given [1, 5, 7, 8], you should return False.

В массиве есть место fixed-point, это такое место
где индекс элемента равен самому элементу.
Нужно написать функцию поиска этого элемента.
Эта функция принимает на вход массив, содержащий УНИКАЛЬНЫЕ элементы
ОТСОРТИРОВАННЫЕ по возрастанию.
Функция должна вернуть этот элемент, или False если такого не найдено
Например:
[-6, 0, 2, 40] -> return 2
[1, 5, 7, 8] -> return False
'''
import pickle
from datetime import datetime


with open('arr2.pkl', 'rb') as file:
    test_arr = pickle.load(file)


# def get_fixed_point(arr):
#     for id, item in enumerate(arr):
#         if id == item:
#             return id
#     return False


def get_fixed_point(array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] < mid:
            low = mid + 1
        elif array[mid] > mid:
            high = mid - 1
        else:
            return array[mid]
    return False


start = datetime.now()
result = get_fixed_point(test_arr)
finish = datetime.now() - start
print(f'Result func1 => {result}  time: {finish}')


assert get_fixed_point(test_arr) == 648639
assert get_fixed_point([-3, -1, 0, 2, 3, 4, 6]) == 6
assert get_fixed_point([0, 2, 4, 6, 8, 10, 16]) == 0
assert get_fixed_point([-3, -1, 0, 2, 3, 5, 9]) == 5
assert get_fixed_point([-3, -1, 0, 2, 4, 7, 9]) == 4
assert get_fixed_point([-3, -1, 0, 2, 4, 7, 9, 25, 31]) == 4
assert get_fixed_point([-3, -1, 0, 2, 3, 5]) == 5
assert get_fixed_point([-3, -1, 0, 2, 3, 9]) is False
