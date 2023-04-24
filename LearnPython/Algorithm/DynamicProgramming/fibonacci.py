def fib_memo(n, cache):
    if n < 3:
        return 1
        
    if n in cache:
        return cache[n]
    
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]

def fib(n):
    fib_cache = {}

    return fib_memo(n, fib_cache)

def fib_tab(n):
    fib_table = [0, 1, 1]

    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    return fib_table[n]

def fib_optimized(n):
    previous = 1
    current = 1
    for i in range(2, n):
        previous, current = current, previous + current
    
    return current