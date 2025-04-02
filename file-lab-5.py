fhand = open('text-file-matrix.txt')
file_text = fhand.read()
print('Number of Characters = ', len(file_text))
print(file_text[file_text.find("red pill"):file_text.find("red pill")+8], [file_text.find("red pill"), file_text.find("red pill") + 8])
