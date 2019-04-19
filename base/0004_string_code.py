# Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('支持中文str')

# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(chr(98))
print('\u4e2d\u6587')

# 区分'ABC'和b'ABC'，前者是 str，后者 是 bytes ，每个字符都只占用一个字节
print('ABC')
print(b'ABC')

# 字节
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print('AAA中文'.encode('utf-8'))
# 会报错
# print('中文'.encode('ascii'))

# 编码
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
# 1个中文字符经过 UTF-8 编码后通常会占用 3 个字节，而 1 个英文字符只占用 1 个字节。
print(len('ABC'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))


# 格式化
print('hi %s , you have %d apples.score is %f ' % ('Jack', 11, 5.5))

