append_text = '\nThis is append text'

file = open('file_01.txt', 'a')
file.write(append_text)
file.close()