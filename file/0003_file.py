file = open('file_01.txt', 'r')
text = file.read()
print(text)

file = open('file_01.txt', 'r')

text_list = file.readlines()
for t in text_list:
    print(t)

file.close()


