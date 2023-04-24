def insertion_sort(random_list):

    sorted_list = list(random_list)

    for i, current in enumerate(sorted_list[1:], 1):
        j = i - 1
        while j >= 0 and sorted_list[j] > current:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = current

    return sorted_list