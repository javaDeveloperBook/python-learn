try:
    file = open('ee.txt', 'r')
except Exception as e:
    print(e)
    file = open('ee.txt', 'w')
    file.write('AAAA')
else:
    text = file.read()
    print(text)
