import random
import time


def bubble_sort(li: list) -> list:
    is_finished = True
    while is_finished:
        is_finished = False
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                is_finished = True
    return li


def quick_sort(li: list) -> list:
    if len(li) <= 1:
        return li
    pivot = random.choice(li)

    left = []
    right = []
    count = 0
    for e in li:
        if e < pivot:
            left.append(e)
        elif e > pivot:
            right.append(e)
        else:
            count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot] * count + right


def selection_sort(li: list) -> list:
    for i, e in enumerate(li):
        target_index = min(range(i, len(li)))
        li[i], li[target_index] = li[target_index], e
    return li


def insertion_sort(li: list) -> list:
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[i] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]
    return li


def merge_sort(li: list) -> list:
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    left, right = li[:mid], li[mid:]
    left, right = merge_sort(left), merge_sort(right)
    return list(merge(left, right))


def merge(left: list, right: list) -> list:
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(right)
    sorted_list.extend(left)
    return sorted_list


if __name__ == '__main__':
    test_list = [3, 6, 7, 1, 2, 10, 8, 9, 2, 9]
    start = time.time()
    print(quick_sort(test_list))
    print(time.time() - start)

    start = time.time()
    print(bubble_sort(test_list))
    print(time.time() - start)

    start = time.time()
    print(selection_sort(test_list))
    print(time.time() - start)

    start = time.time()
    print(insertion_sort(test_list))
    print(time.time() - start)

    start = time.time()
    print(merge_sort(test_list))
    print(time.time() - start)
