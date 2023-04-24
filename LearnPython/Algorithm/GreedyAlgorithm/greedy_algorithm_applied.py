def min_fee(pages_to_print):
    sorted_list = sorted(pages_to_print)

    total_fee = 0

    for i in range(len(sorted_list)):
        total_fee += sorted_list[i] * (len(sorted_list) - i)

    return total_fee

def course_selection(course_list):
    sorted_list = sorted(course_list, key=lambda x: x[1])

    my_selection = [sorted_list[0]]

    for course in sorted_list:
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection