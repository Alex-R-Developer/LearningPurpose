def read_image(filepath):
    img = []
    with open(filepath, 'r') as f:
        data = f.readlines()

    for row in data:
        row = row[:-1]
        img.append([int(bit) for bit in row])
    return img


def save_image(img, filepath):
    with open(filepath, 'w') as f:
        for row in img:
            line = ''
            for bit in row:
                line += str(bit)
            line += '\\\\\\\\n'
            f.write(line)
