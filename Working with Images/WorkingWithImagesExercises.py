from PIL import Image


word_matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

print(word_matrix.size)
print(mask.size)

# Resize mask image to word_matrix size

enlarged_mask = word_matrix.resize((1015, 559))

enlarged_mask.putalpha(200)


# Paste mask picture to shrunk matrix

word_matrix.paste(enlarged_mask, (0,0), enlarged_mask)
word_matrix.show()
