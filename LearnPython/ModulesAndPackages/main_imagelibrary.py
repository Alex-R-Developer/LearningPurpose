import imagelibrary

logo = imagelibrary.read_image('logo')
text = imagelibrary.read_image('text')

upside_down_logo = imagelibrary.vertical_flip(logo)
reversed_text = imagelibrary.horizontal_flip(text)

inverted_text = imagelibrary.invert(text)

merged_img = imagelibrary.merge(logo, text)


print('logo:')
imagelibrary.display(logo)
print('\nlogo vertically flipped:')
imagelibrary.display(upside_down_logo)

print('\ntext:')
imagelibrary.display(text)
print('\ntext horizontally flipped:')
imagelibrary.display(reversed_text)

print('\ntext color inverted:')
imagelibrary.display(inverted_text)

print('\nimage merged:')
imagelibrary.display(merged_img)

print()
key_functions = ['read_image', 'save_image', 'display', 'invert', 'merge', 'horizontal_flip', 'vertical_flip']
non_key_functions = ['get_size', 'empty_image', 'invert_bit', 'or_bits']
print(all(x in dir(imagelibrary) for x in key_functions))
print(not any(x in dir(imagelibrary) for x in non_key_functions))