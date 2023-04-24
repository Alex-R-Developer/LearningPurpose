def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def partition(my_list, start, end):
    i = start
    b = start
    p = end

    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    swap_elements(my_list, b, p)
    p = b

    return p


def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) - 1

    if end - start < 1:
        return

    pivot = partition(my_list, start, end)

    quicksort(my_list, start, pivot - 1)

    quicksort(my_list, pivot + 1, end)