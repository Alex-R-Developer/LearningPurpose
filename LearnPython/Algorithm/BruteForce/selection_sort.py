def selection_sort(random_list):

    sorted_list = list(random_list)

    for i in range(len(sorted_list)):
        min_index = i
        for j in range(i+1, len(sorted_list)):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list