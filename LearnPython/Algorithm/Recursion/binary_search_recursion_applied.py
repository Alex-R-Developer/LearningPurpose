def binary_search(element, some_list, start_index = 0, end_index = None):
    
    if end_index == None:
        end_index = len(some_list) - 1

    if start_index > end_index:
        return None

    midpoint = (start_index + end_index) // 2
    if some_list[midpoint] == element:
        return midpoint
    elif some_list[midpoint] > element:
        return binary_search(element, some_list, start_index, midpoint - 1)
    else:
        return binary_search(element, some_list, midpoint + 1, end_index)