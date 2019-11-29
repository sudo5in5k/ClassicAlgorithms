import random


def bubble_sort(li: list):
    is_finished = True
    while is_finished:
        is_finished = False
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                is_finished = True
    return li


def quick_sort(li: list):
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


def selection_sort(li: list):
    for i, e in enumerate(li):
        target_index = min(range(i, len(li)))
        li[i], li[target_index] = li[target_index], e
    return li


if __name__ == '__main__':
    test_list = [3, 6, 7, 1, 2, 10, 8, 9, 2, 9]
    print(quick_sort(test_list))
    print(bubble_sort(test_list))
    print(selection_sort(test_list))
