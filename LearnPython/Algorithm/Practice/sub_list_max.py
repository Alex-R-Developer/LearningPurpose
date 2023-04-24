def max_crossing_sum(profits, start, end):
    mid = (start + end) // 2

    left_sum = 0
    left_max = profits[mid]

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    right_sum = 0
    right_max = profits[mid + 1]

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def sublist_max(profits, start, end):
    if start == end:
        return profits[start]

    mid = (start + end) // 2

    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    return max(max_left, max_right, max_cross)
    

def sublist_max(profits):
    current_max = profits[0]
    max_profit = profits[0]

    for i in range(1, len(profits)):
        current_max = max(profits[i], current_max + profits[i])
        max_profit = max(max_profit, current_max)

    return max_profit