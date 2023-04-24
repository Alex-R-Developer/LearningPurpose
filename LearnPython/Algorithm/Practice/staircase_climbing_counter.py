def memo_staircase(n, cache, possible_steps):
    if n in cache:
        return cache[n]
    
    if n < 2:
        return 1

    cache[n] = sum(memo_staircase(n - step, cache, possible_steps) for step in possible_steps if step <= n)
    
    return cache[n]
    
def staircase(stairs, possible_steps):
    
    cache = dict()
    
    return memo_staircase(stairs, cache, possible_steps)
    

def staircase(stairs, possible_steps):
    number_of_ways = [1, 1]
    
    for height in range(2, stairs + 1):
        number_of_ways.append(0)

        for step in possible_steps:
            if height - step >= 0:
                number_of_ways[height] += number_of_ways[height - step]

    return number_of_ways[stairs]