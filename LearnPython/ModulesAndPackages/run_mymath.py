from mymath import *


def main():
    x = float(input('Please enter the diameter of a circle: '))
    print('The area of a circle with a diameter of {} is {}.\n'.format(x, shapes.area.circle(x)))

    y = float(input('Please enter the length of a side of a square: '))
    print('The area of a square with a side length of {} is {}.'.format(y, shapes.area.square(y)))


if __name__ == '__main__':
    main()
