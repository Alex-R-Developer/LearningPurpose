def merge(list1, list2):
    i = 0
    j = 0

    merged_list = list()

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    if len(list1) > i:
        merged_list += list1[i:]
    else:
        merged_list += list2[j:]

    return merged_list

def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list

    mid = len(my_list) // 2
    left_half = my_list[:mid]
    right_half = my_list[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))