from collections import deque

def parentheses_checker(string):

    stack = deque()

    print(f"Test string: {string}") 

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            if stack:
                stack.pop()
            else:
                print(f"No opening parenthesis matches the closing parenthesis at position {i} in the string.")

    while stack:
        print(f"The parenthesis at position {stack.pop()} in the string is not closed.")
