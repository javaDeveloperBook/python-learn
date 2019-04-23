# 直接赋值
import copy

a = [1, 2, ['a', 'b']]
b = a

print(id(a) == id(b))
b[0] = 111
print(a)

# 浅拷贝 copy.copy()

c = copy.copy(a)
print(id(c) == id(a))
# 不会改变 a 第一层
c[0] = 1111111
print(a)

# 会改变第二层内容
c[2][0] = 'aaa'
print(a)


# 深拷贝
e = copy.deepcopy(a)
print(id(e) == id(a))

e[2][0] = 'ZZZ'
print(e)
print(a)
