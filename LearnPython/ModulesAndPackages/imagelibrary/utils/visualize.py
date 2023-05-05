def display(img):
    height, width = len(img), len(img[0])
    for i in range(height):
        for j in range(width):
            print(img[i][j], end=' ')
        print()