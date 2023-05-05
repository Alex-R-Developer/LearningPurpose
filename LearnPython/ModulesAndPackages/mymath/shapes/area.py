from mymath.shapes import PI


def circle(radius):
    return PI * radius * radius


def square(length):
    return length * length


def main():
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)

    print(square(2) == 4)
    print(square(5) == 25)


if __name__ == '__main__':
    main()