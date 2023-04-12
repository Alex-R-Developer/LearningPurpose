def remove_empty_lines(input_file_path, output_file_path=None):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    # remove duplicate blank lines
    modified_text = '\n'.join(line for line in text.splitlines() if line.strip())

    # write modified text to output file
    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_text)

    return modified_text
