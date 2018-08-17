# -*-coding:utf-8-*-


def quick_sort(array, left, right):
    if left >= right:
        return
    i = left
    j = right
    p = left
    m = array[left]
    b = []
    while i < j:
        while i < j and array[i] <= m:
            p = i
            i += 1
        while i < j and array[j] >= m:
            j -= 1
        if i < j:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
    array[left] = array[p]
    array[p] = m
    quick_sort(array, left, p-1)
    quick_sort(array, p+1, right)


def stable_quick_sort(array, left, right):
    if left >= right:
        return
    i = left
    j = right
    p = left
    m = array[left]

    left_hole = []
    right_cache = []
    right_hole = []
    left_cache = []

    while i < j:
        while i < j and array[i] <= m:
            p = i
            i += 1
        while i < j and array[j] >= m:
            j -= 1

        if i < j:
            right_cache.append(array[i])
            left_hole.append(i)
            p = i
            i += 1
            left_cache.append(array[j])
            right_hole.append(j)
            j -= 1

    left_cache.reverse()
    right_hole.reverse()

    for (i, j) in zip(left_hole, left_cache):
        array[i] = j

    for (i, j) in zip(right_hole, right_cache):
        array[i] = j

    array[left] = array[p]
    array[p] = m
    stable_quick_sort(array, left, p-1)
    stable_quick_sort(array, p+1, right)


def heap_sort(array):
    array_length = len(array)
    if array is None or array_length <= 0:
        return

    for i in range(array_length/2 - 1, -1, -1):
        max_heap(array, i, array_length)

    for i in reversed(range(array_length)):
        tmp = array[0]
        array[0] = array[i]
        array[i] = tmp
        max_heap(array, 0, i)


def max_heap(array, hole, array_length):
    max_index = hole
    left = 2*hole + 1
    right = 2*hole + 2

    if left < array_length and array[max_index] < array[left]:
        max_index = left
    if right < array_length and array[max_index] < array[right]:
        max_index = right

    if max_index != hole:
        tmp = array[hole]
        array[hole] = array[max_index]
        array[max_index] = tmp
        max_heap(array, max_index, array_length)


if __name__ == "__main__":
    array = [4, 2, 5, 6, 1, 7, 8]
    # heap_sort(array)

    stable_quick_sort(array, 0, len(array)-1)
    print array
