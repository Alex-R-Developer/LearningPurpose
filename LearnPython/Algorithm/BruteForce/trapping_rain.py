def trapping_rain(buildings):
    total_height = 0

    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i + 1:])

        upper_bound = min(max_left, max_right)

        total_height += max(0, upper_bound - buildings[i])

    return total_height
