import random
import Algorithm_test as test

array_length = 20
array = []
maximal = 999999
minimal = -999999

array = [random.randint(minimal, maximal) for i in range(array_length)]

print(array, 'Unsorted array')

# Bubble Sort (Сортировка пузырьком)


def bubble_sort(array):
    sorted_array = array.copy()
    if len(sorted_array) == 1:
        return sorted_array
    elif len(sorted_array) == 2 and sorted_array[0] > sorted_array[1]:
        sorted_array[0], sorted_array[1] = sorted_array[1], sorted_array[0]
        return sorted_array
    else:
        for i in range(array_length - 1):
            for j in range(array_length - i - 1):
                if sorted_array[j] > sorted_array[j + 1]:
                    sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

        return sorted_array

# Selection Sort (Сортировка выбором)


def selection_sort(array):
    sorted_array = array.copy()
    if len(sorted_array) == 1:
        return sorted_array
    elif len(sorted_array) == 2 and sorted_array[0] > sorted_array[1]:
        sorted_array[0], sorted_array[1] = sorted_array[1], sorted_array[0]
        return sorted_array
    else:
        for i in range(array_length):
            minimal_index = i
            for j in range(i + 1, array_length):
                if sorted_array[minimal_index] > sorted_array[j]:
                    minimal_index = j
            sorted_array[i], sorted_array[minimal_index] = sorted_array[minimal_index], sorted_array[i]

        return sorted_array

# Insert Sort (Сортировка вставками)


def insert_sort(array):
    sorted_array = array.copy()
    if len(sorted_array) == 1:
        return sorted_array
    elif len(sorted_array) == 2 and sorted_array[0] > sorted_array[1]:
        sorted_array[0], sorted_array[1] = sorted_array[1], sorted_array[0]
        return sorted_array
    else:
        for i in range(1, array_length):
            elem = sorted_array[i]
            j = i
            while j >= 1 and sorted_array[j - 1] > elem:
                sorted_array[j] = sorted_array[j-1]
                j -= 1
            sorted_array[j] = elem

        return sorted_array

# Binary Insert Sort (Сортировка бинарными вставками)


def binary_search(array, value, left, right):
    if left == right:
        if array[left] > value:
            return left
        else:
            return left + 1
    elif left > right:
        return left

    middle = (left + right) // 2

    if array[middle] < value:
        return binary_search(array, value, middle + 1, right)
    elif array[middle] > value:
        return binary_search(array, value, left, right - 1)
    else:
        return middle


def binary_insert_sort(array):
    sorted_array = array.copy()
    if len(sorted_array) <= 1:
        return sorted_array
    elif len(sorted_array) == 2 and sorted_array[0] > sorted_array[1]:
        sorted_array[0], sorted_array[1] = sorted_array[1], sorted_array[0]
        return sorted_array
    else:
        for i in range(1, array_length):
            value = sorted_array[i]
            j = binary_search(sorted_array, value, 0, i -1)
            sorted_array = sorted_array[:j] + [value] + sorted_array[j:i] + sorted_array[i+1:]

        return sorted_array
        

# Merge sort (Сортировка слиянием)


def merge(array1, array2):
    merged_array = []
    pointer1 = pointer2 = 0
    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] < array2[pointer2]:
            merged_array.append(array1[pointer1])
            pointer1 += 1
        else:
            merged_array.append(array2[pointer2])
            pointer2 += 1
    if pointer1 < len(array1):
        merged_array += array1[pointer1:]
    if pointer2 < len(array2):
        merged_array += array2[pointer2:]

    return merged_array


def merge_sort(array):
    sorted_array = array.copy()
    if len(sorted_array) == 1:
        return sorted_array
    elif len(sorted_array) == 2 and sorted_array[0] > sorted_array[1]:
        sorted_array[0], sorted_array[1] = sorted_array[1], sorted_array[0]
        return sorted_array
    else:
        middle = len(sorted_array) // 2
        left = merge_sort(sorted_array[:middle])
        right = merge_sort(sorted_array[middle:])

        return merge(left, right)


# Quick sort (Быстрая сортировка)

def quick_sort(array):
    sorted_array = array.copy()
    if len(sorted_array) <= 1:
        return sorted_array
    elif len(sorted_array) == 2 and sorted_array[0] > sorted_array[1]:
        sorted_array[0], sorted_array[1] = sorted_array[1], sorted_array[0]
        return sorted_array
    else:
        element = sorted_array[0]
        left = []
        equal = []
        right = []
        for i in sorted_array:
            if i > element:
                right.append(i)
            elif i < element:
                left.append(i)
            else:
                equal.append(i)

        return quick_sort(left) + equal + quick_sort(right)


print(bubble_sort(array), 'Bubble Sort')
print(selection_sort(array), 'Selection Sort')
print(insert_sort(array), 'Insert Sort')
print(binary_insert_sort(array), 'Binary insert Sort')
print(merge_sort(array), 'Merge Sort')
print(quick_sort(array), 'Quick Sort')

print('Sorting test')
print(test.test(quick_sort))