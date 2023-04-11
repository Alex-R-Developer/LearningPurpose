# Basic Calculator
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide_new(a, b):  
    return a/b

def get_Median(a, b):
    return (a+b)/2

def getSum_ver2(n):
    sum = 0
    
    for i in range(1, n+1):
        sum = sum + i

    return sum
