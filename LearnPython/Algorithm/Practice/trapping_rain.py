def trapping_rain(buildings):
    total_height = 0

    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i + 1:])

        upper_bound = min(max_left, max_right)

        total_height += max(0, upper_bound - buildings[i])

    return total_height

def trapping_rain(buildings):
    total_height = 0 
    n = len(buildings)

    left_list = [0] * n
    right_list = [0] * n

    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i-1], buildings[i-1])
                
    right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i+1], buildings[i+1])

    for i in range(1, n-1):
        upper_bound = min(right_list[i], left_list[i])

        total_height += max(0, upper_bound - buildings[i])

    return total_height

def trapping_rain(buildings):
    
    highest_so_far = buildings[0], 0
    higher_than_previous = None
    potential_level = 0
    water_level = 0
    
    for i, current in enumerate(buildings):
        if i == 0:
            continue
        if current > highest_so_far[0]:
            water_level += potential_level
            potential_level = 0
            highest_so_far = current, i
        elif current > buildings[i - 1]:
            higher_than_previous = current, i
            water_level += potential_level - (highest_so_far[0] - current) * (i - highest_so_far[1] - 1)
            potential_level = (highest_so_far[0] - current) * (i - highest_so_far[1] - 1) + highest_so_far[0] - current
        else:
            potential_level += highest_so_far[0] - current

    return water_level