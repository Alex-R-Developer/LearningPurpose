def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    
def partition(my_list, start, end):
    i = start
    b = start
    
    while i < end:
        if my_list[i] <= my_list[end]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
        
    swap_elements(my_list, b, end)

    return b
    
def quicksort(my_list, start = 0, end = None):
    if end is None:
        end = len(my_list) - 1
    
    if not (start < end):
        return
    
    pivot = partition(my_list, start, end)
    left_half = quicksort(my_list, start, pivot - 1)
    right_half = quicksort(my_list, pivot + 1, end)