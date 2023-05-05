__all__ = ["invert", "merge", "horizontal_flip", "vertical_flip"]


def invert(img):
    height, width = len(img), len(img[0])
    new_img = empty_image(height, width)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = invert_bit(img[i][j])
    return new_img


def merge(img1, img2):
    if get_size(img1) == get_size(img2):
        [height, width] = get_size(img1)
        new_img = empty_image(height, width)
        for i in range(height):
            for j in range(width):
                new_img[i][j] = or_bits(img1[i][j], img2[i][j])
        return new_img
    else:
        print("Size of images must be the same!")


def horizontal_flip(img):
    [height, width] = get_size(img)
    new_img = empty_image(height, width)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = img[i][width-j-1] 
    return new_img


def vertical_flip(img):
    [height, width] = get_size(img)
    new_img = empty_image(height, width)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = img[height-i-1][j] 
    return new_img


def get_size(img):
    return [len(img), len(img[0])]


def empty_image(height, width):
    new_img = []
    for i in range(height):
        new_img.append([-1] * width)
    return new_img


def invert_bit(bit):
    return 1 - bit


def or_bits(bit1, bit2):
    return min(1, bit1 + bit2)