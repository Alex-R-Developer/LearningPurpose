def max_profit_memo(price_list, count, cache):
    if count in cache:
        return cache[count]

    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        
        profit = max(profit, max_profit_memo(price_list, i, cache) 
                 + max_profit_memo(price_list, count - i, cache))
        
    cache[count] = profit
    
    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)

def max_profit(price_list, count):
    profit_table = list()

    for i in range(1, count + 1): 
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0

        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)

    return profit_table[count]
