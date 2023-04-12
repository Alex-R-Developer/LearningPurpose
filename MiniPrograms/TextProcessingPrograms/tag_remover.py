def remove_tags(input_file_path, output_file_path=None):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    # remove text between <>
    modified_text = ''
    i = 0
    while i < len(text):
        if text[i] == '<':
            j = text.find('>', i)
            i = j + 1
            modified_text += "\n"
        else:
            modified_text += text[i]
            i += 1

    # write modified text to output file
    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_text)

    return modified_text
